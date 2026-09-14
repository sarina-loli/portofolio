import "./states.css";

export default function Loading({ label = "Loading" }) {
  return (
    <div className="state state-loading" role="status" aria-live="polite">
      <span className="state-spinner" aria-hidden="true" />
      <span>{label}…</span>
    </div>
  );
}
