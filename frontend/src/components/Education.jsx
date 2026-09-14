import Loading from "./Loading";
import ErrorState from "./ErrorState";
import EmptyState from "./EmptyState";
import "./Education.css";

function formatDate(value) {
  if (!value) return "Present";
  return new Date(value).toLocaleDateString(undefined, { year: "numeric", month: "short" });
}

export default function Education({ education, loading, error, onRetry }) {
  return (
    <section id="education" className="section education">
      <div className="container">
        <div className="section-head">
          <p className="kicker">Education</p>
          <h2>Academic background</h2>
        </div>

        {loading && <Loading label="Loading education" />}
        {error && <ErrorState message="Couldn't load education from the API." onRetry={onRetry} />}
        {!loading && !error && education?.length === 0 && <EmptyState title="Nothing listed yet" />}

        {!loading && !error && education?.length > 0 && (
          <div className="education-grid">
            {education.map((item) => (
              <div className="education-card card" key={item.id}>
                <span className="education-dates">
                  {formatDate(item.start_date)} — {formatDate(item.end_date)}
                </span>
                <h3>{item.degree}</h3>
                <p className="education-institution">{item.institution}</p>
                {item.description && <p>{item.description}</p>}
              </div>
            ))}
          </div>
        )}
      </div>
    </section>
  );
}
