import "./states.css";

export default function EmptyState({ title = "Nothing here yet", message }) {
  return (
    <div className="state state-empty">
      <p className="state-title">{title}</p>
      {message && <p className="state-message">{message}</p>}
    </div>
  );
}
