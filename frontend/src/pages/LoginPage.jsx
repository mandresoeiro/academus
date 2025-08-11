import { useState } from "react";
import { login } from "../services/api";
import { saveToken } from "../services/authService";
import { useUser } from "../context/UserContext";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { setUser } = useUser();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await login(username, password);
      saveToken(res.data.key);
      setUser(username);
      navigate("/dashboard");
    } catch {
      setError("Usuário ou senha inválidos");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <form onSubmit={handleSubmit} className="bg-white p-8 rounded shadow-md w-full max-w-sm">
        <h2 className="text-2xl font-bold mb-6 text-center">Entrar no Academus</h2>
        <input
          placeholder="Usuário"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full px-4 py-2 mb-4 border border-gray-300 rounded"
        />
        <input
          type="password"
          placeholder="Senha"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full px-4 py-2 mb-4 border border-gray-300 rounded"
        />
        <button type="submit" className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">
          Entrar
        </button>
        {error && <p className="text-red-500 text-sm mt-2 text-center">{error}</p>}
      </form>
    </div>
  );
}
