import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const askTruthGuard = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/ask",
        {
          question: question,
        }
      );

      setResult(response.data);
    } catch (error) {
      setResult({
        error: "Unable to connect to TruthGuard backend.",
      });
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <header>
        <h1>TruthGuard</h1>
        <p>
          Self-Verifying RAG Engine for Hallucination Detection
        </p>
      </header>

      <main>
        <div className="question-box">
          <textarea
            placeholder="Ask TruthGuard a question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />

          <button onClick={askTruthGuard} disabled={loading}>
            {loading ? "Analyzing..." : "Ask TruthGuard"}
          </button>
        </div>

        {result && (
          <div className="result">
            <h2>Result</h2>

            {result.error ? (
              <p>{result.error}</p>
            ) : (
              <>
                <p>
                  <strong>Question:</strong> {result.question}
                </p>

                <p>
                  <strong>Answer:</strong> {result.answer}
                </p>

                <p>
                  <strong>Status:</strong> {result.status}
                </p>

                <p>
                  <strong>Truth Probability:</strong>{" "}
                  {result.truth_probability}
                </p>
              </>
            )}
          </div>
        )}
      </main>
    </div>
  );
}

export default App;