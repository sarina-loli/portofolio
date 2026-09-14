import "./About.css";

export default function About({ profile }) {
  return (
    <section id="about" className="section about">
      <div className="container about-grid">
        <div className="section-head">
          <p className="kicker">About</p>
          <h2>The short version</h2>
          <p>{profile?.about}</p>
        </div>

        <div className="about-details">
          {profile?.philosophy && (
            <div className="about-block">
              <h3>Development philosophy</h3>
              <p>{profile.philosophy}</p>
            </div>
          )}
          {profile?.specialties && (
            <div className="about-block">
              <h3>What I specialize in</h3>
              <p>{profile.specialties}</p>
            </div>
          )}
          {profile?.career_goals && (
            <div className="about-block">
              <h3>Where I'm headed</h3>
              <p>{profile.career_goals}</p>
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
