import "./GithubSection.css";

export default function GithubSection({ profile, featuredProjects = [] }) {
  if (!profile?.github_url) return null;

  return (
    <section id="github" className="section github-section">
      <div className="container github-inner card">
        <div className="github-copy">
          <p className="kicker">Open source</p>
          <h2>See the code behind these projects</h2>
          <p>
            Every project here has a public repository. Browse commit history, issues,
            and the rest of what I&rsquo;ve shipped on GitHub.
          </p>
          <a href={profile.github_url} target="_blank" rel="noreferrer" className="btn btn-accent">
            View GitHub profile
          </a>
        </div>

        {featuredProjects.length > 0 && (
          <ul className="github-repos">
            {featuredProjects.slice(0, 4).map((project) => (
              <li key={project.id} className="github-repo">
                <a href={project.github_url || profile.github_url} target="_blank" rel="noreferrer">
                  {project.title}
                </a>
                <div className="github-repo-tech">
                  {project.technologies?.slice(0, 3).map((tech) => (
                    <span key={tech.id} className="pill">{tech.name}</span>
                  ))}
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </section>
  );
}
