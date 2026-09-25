import "./Hero.css";

export default function Hero({ profile }) {
  const name = profile?.full_name || "Sara Getu";
  const firstName = name.split(" ")[0];
  const intro =
    profile?.intro ||
    `Hi, I'm ${name}. I'm a Full-Stack Software Developer specializing in building modern, secure, and scalable web applications using React, Django, and Django REST Framework.`;

  return (
    <section className="hero">
      <div className="container hero-inner">
        <div className="hero-copy">
          <p className="kicker">{profile?.title || "Full-Stack Software Developer"}</p>
          <h1>
            Hi, I&rsquo;m {firstName}.
            <br />I build software people can rely on.
          </h1>
          <p className="hero-intro">{intro}</p>

          <div className="hero-actions">
            <a href="/#projects" className="btn btn-primary">View my projects</a>
            <a href="/#contact" className="btn btn-outline">Contact me</a>
            {profile?.resume && (
              <a href={profile.resume} className="btn btn-outline" download>
                Download resume
              </a>
            )}
          </div>

          <div className="hero-social">
            {profile?.github_url && (
              <a href={profile.github_url} target="_blank" rel="noreferrer">GitHub ↗</a>
            )}
            {profile?.linkedin_url && (
              <a href={profile.linkedin_url} target="_blank" rel="noreferrer">LinkedIn ↗</a>
            )}
            {profile?.tiktok_url && (
              <a href={profile.tiktok_url} target="_blank" rel="noreferrer"><span className="tiktok-text">TikTok ↗</span></a>
            )}
          </div>
        </div>
        <div className="hero-loading-message">
          {profile?.hello || "Please wait while everything loads... ⏳"}
        </div>

        <div className="hero-visual" aria-hidden="true">
          <div className="code-window card">
            <div className="code-window-bar">
              <span className="dot dot-red" />
              <span className="dot dot-amber" />
              <span className="dot dot-green" />
              <span className="code-window-title">developer.py</span>
            </div>
            <pre className="code-window-body">
<span className="tok-kw">class</span> <span className="tok-class">Developer</span>:
    <span className="tok-kw">def</span> <span className="tok-fn">__init__</span>(<span className="tok-self">self</span>):
        <span className="tok-self">self</span>.stack = [<span className="tok-str">"React"</span>, <span className="tok-str">"Django"</span>, <span className="tok-str">"PostgreSQL"</span>]
        <span className="tok-self">self</span>.focus = <span className="tok-str">"secure, scalable APIs"</span>

    <span className="tok-kw">def</span> <span className="tok-fn">ship</span>(<span className="tok-self">self</span>, idea):
        <span className="tok-kw">return</span> <span className="tok-fn">build</span>(idea, tested=<span className="tok-kw">True</span>)
            </pre>
          </div>
        </div>
      </div>
    </section>
  );
}
