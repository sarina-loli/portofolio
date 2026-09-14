import { useEffect, useState } from "react";

/**
 * Runs an async fetcher on mount (and whenever deps change), tracking
 * loading / error / data state. Guards against setting state after unmount.
 */
export default function useFetch(fetcher, deps = []) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let alive = true;
    setLoading(true);
    setError(null);

    fetcher()
      .then((result) => {
        if (alive) setData(result);
      })
      .catch((err) => {
        if (alive) setError(err);
      })
      .finally(() => {
        if (alive) setLoading(false);
      });

    return () => {
      alive = false;
    };
    // Deps are provided by the caller to control when this re-runs.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [...deps]);

  return { data, error, loading };
}
