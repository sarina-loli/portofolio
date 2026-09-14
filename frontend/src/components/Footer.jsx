import "./Footer.css";

export default function Footer({ profile }) {
  const year = new Date().getFullYear();
  const name = profile?.full_name || "Alex Morgan";

  return (
    <footer className="footer">
      <div className="container footer-inner">
        <div>
          <p className="footer-name">{name}</p>
          <p className="footer-tagline">
            {profile?.tagline || "Full-Stack Software Developer."}
          </p>
        </div>

        <nav className="footer-links" aria-label="Footer">
          <a href="/#about">About</a>
          <a href="/#projects">Projects</a>
          <a href="/#experience">Experience</a>
          <a href="/#contact">Contact</a>
        </nav>

        <div className="footer-contact">
          {profile?.github_url && (
            <a href={profile.github_url} target="_blank" rel="noreferrer">GitHub</a>
          )}
          {profile?.linkedin_url && (
            <a href={profile.linkedin_url} target="_blank" rel="noreferrer">LinkedIn</a>
          )}
          {profile?.email && <a href={`mailto:${profile.email}`}>{profile.email}</a>}
        </div>
      </div>

      <div className="container footer-bottom">
        <p>© {year} {name}. All rights reserved.</p>
      </div>
    </footer>
  );
}
