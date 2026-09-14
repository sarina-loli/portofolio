import "./states.css";

export default function ErrorState({
  title = "Something went wrong",
  message = "That request didn't go through. Check your connection and try again.",
  onRetry,
}) {
  return (
    <div className="state state-error" role="alert">
      <p className="state-title">{title}</p>
      <p className="state-message">{message}</p>
      {onRetry && (
        <button type="button" className="btn btn-outline" onClick={onRetry}>
          Try again
        </button>
      )}
    </div>
  );
}
