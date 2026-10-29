"""Build the research figures from recorded arrays and explicit formulae.

Run from any directory. Outputs: figures/*.svg and figures/*.png.
No PDE solver is run and no stored numerical result is overwritten.
"""
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.ticker import MaxNLocator
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
INK, MUTED = "#172b3a", "#596b79"
TEAL, RUST, BLUE, GOLD = "#087e8b", "#c85b43", "#5468a8", "#b48a36"
PALE, GRID = "#eef5f5", "#dce4e8"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10.5,
    "text.color": INK, "axes.labelcolor": INK,
    "axes.edgecolor": GRID, "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.titleweight": "semibold", "axes.titlesize": 12,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": False, "lines.linewidth": 2,
    "legend.frameon": False, "legend.fontsize": 9,
    "figure.facecolor": "white", "axes.facecolor": "white",
    "savefig.facecolor": "white", "svg.fonttype": "path",
    "mathtext.fontset": "dejavusans",
})
CMAP = LinearSegmentedColormap.from_list("focusing", ["#fafcfc", "#add5d8", TEAL, "#123e59"])
SOURCES = {}


def record(name, files, kind):
    SOURCES[name] = {"kind": kind, "inputs": [str(p) for p in files]}


def load_npz(rel):
    return np.load(ROOT / rel, allow_pickle=False)


def load_json(rel):
    return json.loads((ROOT / rel).read_text())


def canvas(title, subtitle, n=3, height=4.9, widths=None):
    fig, axes = plt.subplots(1, n, figsize=(14, height), gridspec_kw={"width_ratios": widths})
    fig.subplots_adjust(left=.065, right=.97, bottom=.20, top=.72, wspace=.38)
    fig.text(.04, .94, title, fontsize=20, weight="semibold", va="top")
    fig.text(.04, .84, subtitle, fontsize=10.5, color=MUTED, va="top")
    return fig, np.atleast_1d(axes)


def label(ax, letter, title):
    ax.set_title(f"{letter}  {title}", loc="left", pad=12)


def foot(fig, text):
    fig.text(.04, .045, text, color=MUTED, fontsize=9, va="bottom")


def save(fig, name):
    for ext in ("svg", "png"):
        fig.savefig(OUT / f"{name}.{ext}", dpi=160,
                    metadata={"Creator": "Shuxing Yang"} if ext == "svg" else None)
    plt.close(fig)


def coherent_profiles():
    seed = "computations/excited-waves/axial-profiles/round2_radial_mode1_dim4.npz"
    moving = "computations/excited-waves/axial-profiles/round2_N4_axial_N512_L64_v0.02.npz"
    z = load_npz(seed)
    fig, ax = canvas("Negative energy with persistent coherent motion",
        "Biharmonic NLS in four dimensions  |  recorded excited profile and moving-wave computation")
    r, q = z["r"], z["y"][0]
    ax[0].plot(r, q, color=TEAL)
    ax[0].axhline(0, color=GRID, lw=1)
    ax[0].fill_between(r, q, 0, where=q < 0, color=RUST, alpha=.18)
    ax[0].set(xlim=(0, 13), xlabel="Radius $r$", ylabel="Signed amplitude $Q(r)$")
    label(ax[0], "a", "Excited stationary seed")
    z = load_npz(moving)
    x, w = z["x"], z["W"]
    # The saved axial variable is W(x,r)=r U(x,r), not U itself.
    u = np.divide(w, x[None, :], out=np.zeros_like(w), where=x[None, :] != 0)
    j = np.flatnonzero(x == 0)
    if len(j):
        u[:, j[0]] = (w[:, j[0]+1] - w[:, j[0]-1])/(2*(x[1]-x[0]))
    sl = np.flatnonzero(abs(x) <= 9)
    extent = (x[sl[0]], x[sl[-1]], x[sl[0]], x[sl[-1]])
    rho = abs(u[np.ix_(sl, sl)].T)**2
    im = ax[1].imshow(rho/rho.max(), extent=extent, origin="lower", cmap=CMAP)
    ax[1].set(xlabel="Travel direction $x_1$", ylabel="Transverse section $x_2$")
    label(ax[1], "b", r"Moving intensity, $v=0.02$")
    fig.colorbar(im, ax=ax[1], fraction=.044, pad=.025, label="Normalized intensity")
    imq = u[np.ix_(sl, sl)].imag.T / .02
    lim = np.max(abs(imq))
    im = ax[2].imshow(imq, extent=extent, origin="lower", cmap="RdBu_r", vmin=-lim, vmax=lim)
    ax[2].set(xlabel="Travel direction $x_1$", ylabel="Transverse section $x_2$")
    label(ax[2], "c", "Phase response, Im$(U_v)/v$")
    fig.colorbar(im, ax=ax[2], fraction=.044, pad=.025)
    foot(fig, r"Numerical profiles shown. The continuum theorem uses separate certificates: $I<0$, $P_1(U_v)=2Iv+O(v^3)$, $E(U_v)=Iv^2/4+O(v^4)$.")
    save(fig, "coherent-profiles")
    record("coherent-profiles", [seed, moving], "Recorded numerical profiles; theorem stated separately")


def radiation_and_gap():
    fig, ax = canvas("Zero total momentum does not force collapse",
        "A moving excited core can share its momentum budget with dispersive radiation", n=2, widths=[1, 1.15])
    a = np.linspace(.65, 3, 400)
    ax[0].plot(a, a**-3, color=TEAL, label=r"$E_{rad}^{inf}/|E_{core}|=(\mu_{crit}/\mu)^3$")
    ax[0].axhline(1, color=RUST, lw=1.4)
    ax[0].axvline(1, color=GRID, ls=":")
    ax[0].fill_between(a, a**-3, 1, where=a>=1, color=TEAL, alpha=.13)
    ax[0].text(1.48, .62, "Negative total energy\nbecomes feasible", color=TEAL, fontsize=11)
    ax[0].set(xlim=(.65, 3), ylim=(0, 3), xlabel=r"Radiation mass $\mu/\mu_{crit}$", ylabel="Relative radiation energy cost")
    label(ax[0], "a", "Exact free-radiation cost")
    ax[0].legend(loc="upper right", fontsize=9)
    a1 = ax[1]
    a1.set_xlim(0, 10); a1.set_ylim(0, 3.8); a1.axis("off")
    label(a1, "b", "The traveling-profile mass gap")
    a1.annotate("", xy=(9.6,.65), xytext=(.3,.65), arrowprops={"arrowstyle":"->", "color":INK, "lw":1.4})
    a1.plot([2.1, 2.1], [.52,.78], color=INK)
    a1.plot([5.3, 5.3], [.52,.78], color=INK)
    a1.text(2.1,.26,r"$M_c$",ha="center",fontsize=13)
    a1.text(5.3,.26,r"$M_c+\delta$",ha="center",fontsize=13)
    a1.text(9.65,.27,"Mass",ha="right")
    a1.axvspan(2.1, 5.3, ymin=.28, ymax=.69, color=PALE)
    a1.text(3.7,1.92,"No negative-energy\ntraveling profile",ha="center",va="center",color=TEAL,fontsize=12)
    a1.text(7.4,1.92,"Excited coherent motion\nexists at larger mass",ha="center",va="center",fontsize=12)
    a1.annotate("", xy=(5.3,3.02), xytext=(2.1,3.02), arrowprops={"arrowstyle":"<->","color":TEAL})
    a1.text(3.7,3.17,r"Uniform $\delta>0$",ha="center",color=TEAL,fontsize=12)
    a1.text(7.25,2.92,r"$P_{core}+P_{rad}=0$",ha="center",fontsize=12)
    foot(fig, r"Quartic cost: $E_{rad}^{inf}=q^4/(2\mu^3)$ and $\mu_{crit}=q(4/v)^{1/3}$. Right: a schematic mass axis; the gap size is not computed.")
    save(fig, "radiation-and-gap")
    record("radiation-and-gap", ["theory/coherent-radiation/wave-radiation.md", "theory/profile-mass-gap/traveling-mass-gap.md"], "Exact normalized cost and qualitative theorem diagram")


def occupations_and_core():
    src = "computations/occupation-computations/r15_townes_profile.npz"
    z = load_npz(src)
    fig, ax = canvas("Conserved occupations determine which mass can concentrate",
        "The Gram eigenvalues constrain the threshold; the singular core carries the principal occupation")
    p = np.linspace(.15,1,400)
    ax[0].plot(p, 1/p, color=TEAL)
    for m in [1,2,3,4,6]:
        ax[0].scatter([1/m], [m], color=TEAL, s=26, zorder=3)
    ax[0].text(.45,5.35,r"$M_*(p)=M_c/p_1$",fontsize=15,color=TEAL)
    ax[0].text(.45,4.55,"All finite spectra\nin 1D quintic NLS",color=MUTED,fontsize=10)
    ax[0].set(xlim=(.13,1.03),ylim=(.8,7),xlabel=r"Largest occupation $p_1$",ylabel=r"Threshold $M_*/M_c$")
    label(ax[0],"a","Occupation-dependent threshold")
    rr = np.linspace(0,5,600)
    for ell,c in [(1.6,BLUE),(1,TEAL),(.55,RUST)]:
        rho = np.interp(rr/ell,z['r'],z['q'])**2/ell**2
        ax[1].plot(rr,rho,color=c,label=rf"$\lambda={ell:g}$")
    ax[1].set(xlim=(0,4),xlabel="Radius $r$",ylabel=r"2D core density $\lambda^{-2}Q^2(r/\lambda)$")
    label(ax[1],"b","A coherent Townes core")
    ax[1].legend(loc="upper right")
    h=np.linspace(.04,1,200)
    ax[2].plot(h,h,color=TEAL,label=r"$\lambda\sim\mu_*(T-t)$")
    ax[2].plot(h,h*h,color=RUST,ls="--",label=r"$\lambda\sim C(T-t)^2$")
    ax[2].text(.13,.72,"Linear: curvature theorem",color=TEAL,fontsize=10)
    ax[2].text(.4,.13,"Quadratic: proposed orbit",color=RUST,fontsize=10)
    ax[2].set(xlim=(0,1),ylim=(0,1.05),xlabel=r"Time to collapse $T-t$ (scaled)",ylabel="Core width (scaled)")
    label(ax[2],"c","Scale selection")
    foot(fig, "a: 1D sharp input due to Read–Schulz; the same law in 2D is proved here for a separated largest occupation.\n"
              "b: rescaled recorded Townes profile, not a time simulation. c: normalized asymptotic laws; the quadratic-collapse solution is not constructed.")
    save(fig,"occupations-and-core")
    record("occupations-and-core",[src,"theory/occupation-thresholds/occupation-gap.md","theory/background-interaction/modulation.md","theory/background-interaction/quintic-closure.md","manuscripts/fixed-occupation/Fixed-Occupation-Thresholds.tex"],"Threshold formula, profile rescalings, and labeled asymptotic laws")


def hermite_density(path, n=241, limit=9):
    z=load_npz(path); C,ix=z["C"],z["ix"]
    x=np.linspace(-limit,limit,n); cut=int(ix.max())
    h=np.empty((n,cut+1)); h[:,0]=np.pi**(-.25)*np.exp(-x*x/2)
    if cut: h[:,1]=np.sqrt(2)*x*h[:,0]
    for k in range(1,cut):
        h[:,k+1]=np.sqrt(2/(k+1))*x*h[:,k]-np.sqrt(k/(k+1))*h[:,k-1]
    coeff=np.zeros((cut+1,cut+1,C.shape[1]),dtype=C.dtype)
    for k,(a,b) in enumerate(ix): coeff[a,b]=C[k]
    fields=np.einsum("ia,abn,jb->ijn",h,coeff,h,optimize=True)
    return x,np.sum(abs(fields)**2,axis=2)


def collective_binding():
    prefix="computations/hermite-optimization/"
    source=prefix+"r21_orbital_summary.json"
    data=load_json(source)
    rank2=prefix+Path(data['best_per_rank']['2']['coefficients']).name
    rank4=prefix+Path(data['best_per_rank']['4']['coefficients']).name
    fig,ax=canvas("Collective binding: attraction competes with orthogonality",
        "Recorded whole-plane Hermite searches  |  the sharp unrestricted two-dimensional inequality remains open")
    for a,path,rank,letter in [(ax[0],rank2,2,'a'),(ax[1],rank4,4,'b')]:
        x,rho=hermite_density(path)
        im=a.imshow(rho.T/rho.max(),origin="lower",extent=(x[0],x[-1],x[0],x[-1]),cmap=CMAP)
        a.set(xlabel="$x$",ylabel="$y$")
        label(a,letter,f"Computed density, rank {rank}")
    ranks=np.array([int(k) for k in data['best_per_rank']])
    gaps=np.array([data['best_per_rank'][str(k)]['relative_gap'] for k in ranks])
    ax[2].semilogy(ranks,gaps,"o-",color=TEAL,markersize=5)
    ax[2].set(xlabel="Number of orthogonal modes",ylabel=r"Relative gap $1-(F/T)/(2/M_c)$",xticks=ranks)
    ax[2].grid(axis='y',color=GRID,lw=.7,which='major')
    label(ax[2],"c","Best recorded quotient by rank")
    foot(fig,"Finite-basis numerical searches: 61 runs, including 20 stopped at the iteration limit. Splitting is a known numerical phenomenon.\n"
             "The plotted positive gaps describe these candidates; they do not give an upper bound on the variational supremum.")
    save(fig,"collective-binding")
    record("collective-binding",[source,rank2,rank4],"Recorded optimization outputs and reconstructed densities")


def spectral_response():
    source="computations/full-response/r31_response_calibration.json"
    d=load_json(source); a=d['results'][-1]
    quadratic=max(max(a['full_quadratic_radial_eigenvalues']),*(s['ratio'] for s in a['sectors'] if s['name'].startswith('tracefree')))
    common=next(s['ratio'] for s in a['sectors'] if s['name']=='common_scale_control')
    vals=[quadratic,common,max(a['restricted_dilation_response_eigenvalues']),max(a['derivative_response_eigenvalues'])]
    fig,ax=canvas("The response must include unoccupied states",
        "18 October results  |  complete spectral response and an obstruction to a proposed density correction",n=2,widths=[1.3,1])
    labels=["Quadratic potential family","Common-scale control","Restricted dilation response","Full derivative response"]
    colors=[BLUE,MUTED,GOLD,TEAL]
    for i,(v,c) in enumerate(zip(vals,colors)):
        ax[0].plot([.85,v],[i,i],color=c,lw=3)
        ax[0].scatter([v],[i],s=48,color=c,zorder=3)
        ax[0].text(v+.012,i,f"{v:.6f}",va="center",fontsize=10,color=c)
    ax[0].axvline(1,color=RUST,lw=1.3,ls="--")
    ax[0].set(yticks=range(4),yticklabels=labels,xlim=(.84,1.54),ylim=(3.6,-.65),xlabel="Response ratio (instability threshold = 1)")
    ax[0].tick_params(axis='y',length=0)
    label(ax[0],"a","A known three-mode saddle")
    # Universal large-separation shapes after removing their distinct constants.
    r=np.linspace(2,9,250)
    ax[1].semilogy(r,np.exp(-2*r),color=TEAL,label=r"$D/C_D\sim e^{-2R}$")
    ax[1].semilogy(r,np.exp(-r)/np.sqrt(r),color=RUST,label=r"$G/C_G\sim R^{-1/2}e^{-R}$")
    ax[1].set(xlabel="Core separation $R$",ylabel="Normalized leading asymptotic term")
    ax[1].legend(loc='upper right')
    ax[1].grid(axis='y',color=GRID,lw=.7)
    label(ax[1],"b","Separated-core scale mismatch")
    fig.subplots_adjust(left=.19,wspace=.43)
    foot(fig,"a: stored calibration at a = 12.805839 > Mc, R = 65 and h = 0.0025. b: analytical leading terms, not measured finite-separation deficits.\n"
             "Since G decays more slowly than D, every fixed positive linear density-gradient correction fails on sufficiently separated cores.")
    save(fig,"spectral-response")
    record("spectral-response",[source,"theory/full-response/response-schur.md","theory/full-response/density-gradient.md"],"Recorded spectral calibration and analytical asymptotic comparison")


def mixed_dispersion():
    prefix="computations/mixed-dispersion-continuation/core_continuation/"
    fig,ax=canvas("Toward a cubic optical model with mixed dispersion",
        r"One quadratic temporal direction and two quartic transverse directions: $i u_z=(-\partial_\tau^2+\Delta_\perp^2)u-|u|^2u$")
    k=np.linspace(-1.5,1.5,250); xx,yy=np.meshgrid(k,k)
    cs=ax[0].contour(xx,yy,xx**2+yy**4,levels=[.15,.5,1,2,4],colors=[BLUE,TEAL,TEAL,GOLD,RUST],linewidths=1.4)
    ax[0].clabel(cs,inline=True,fontsize=8)
    ax[0].set(xlabel=r"Temporal frequency $\xi_\tau$",ylabel=r"Transverse frequency $\eta$")
    label(ax[0],"a",r"Dispersion $\xi_\tau^2+|\eta|^4$")
    files=[]
    for name,c,lab in [('run128',GOLD,'Finite volume 128'),('refine192',BLUE,'Finite volume 192'),('spectral256',TEAL,'DCT/Bessel 256 × 128')]:
        rel=prefix+name+'/results.json';files.append(rel)
        a=load_json(rel);a=[r for r in a if r.get('residual',1)<1e-6 and 'response_I' in r and r['s']>=.95]
        ax[1].plot([r['s'] for r in a],[r['response_I'] for r in a],'o-',color=c,label=lab,markersize=4)
    ax[1].axhline(0,color=MUTED,lw=1)
    ax[1].axvline(1,color=RUST,ls='--',lw=1.2)
    ax[1].text(.999,490,'Target',rotation=90,ha='right',va='top',color=RUST,fontsize=9)
    ax[1].set(xlim=(.967,1.002),ylim=(-100,530),xlabel="Auxiliary continuation parameter $s$",ylabel=r"Quartic-direction response $I$")
    ax[1].xaxis.set_major_locator(MaxNLocator(4))
    ax[1].legend(loc='lower left',fontsize=8)
    label(ax[1],"b","Recorded approach to $s=1$")
    rel=prefix+'critical128/results.json';files.append(rel);a=load_json(rel)
    rel=prefix+'arc128/results.json';files.append(rel);b=load_json(rel)
    ax[2].plot([r['s'] for r in a],[r['mass'] for r in a],color=BLUE,label='Ordinary continuation')
    ax[2].plot([r['s'] for r in b],[r['mass'] for r in b],color=TEAL,label='Arclength continuation')
    end=b[-1];ax[2].scatter([end['s']],[end['mass']],color=TEAL,s=28)
    ax[2].set(xlim=(-.025,.72),xlabel="Quartic cross-term removal $s$",ylabel="Computed mass")
    ax[2].legend(loc='lower left',fontsize=8)
    label(ax[2],"c","A fold on the separate critical path")
    foot(fig,"b: the auxiliary path is not mass-critical for 0 < s < 1; its coarse negative response changes sign under refinement.\n"
             "c: finite-grid branch geometry. The target optical model has a proved intrinsic-energy mass gap; negative-energy wave existence is unresolved.")
    save(fig,"mixed-dispersion")
    record("mixed-dispersion",files+["theory/coherent-radiation/anisotropic-gap.md"],"Exact dispersion contours and recorded continuation data")


if __name__ == "__main__":
    for plot in (coherent_profiles, radiation_and_gap, occupations_and_core,
                 collective_binding, spectral_response, mixed_dispersion):
        plot()
    (OUT/"sources.json").write_text(json.dumps(SOURCES,indent=2,ensure_ascii=False)+"\n")
    print(f"Built {len(SOURCES)} figures in SVG and PNG.")
