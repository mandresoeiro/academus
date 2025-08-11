import { useState } from "react";
import { login } from "../services/api";
import { saveToken } from "../services/authService";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [user, setUser] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await login(username, password);
      saveToken(res.data.key);
      setUser(username);
    } catch {
      setError("Usuário ou senha inválidos");
    }
  };

  return (
    <div style={{ maxWidth: 300, margin: "auto", marginTop: 100 }}>
      {user ? (
        <div>Bem-vindo, {user}!</div>
      ) : (
        <form onSubmit={handleSubmit}>
          <input
            placeholder="Usuário"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          /><br />
          <input
            type="password"
            placeholder="Senha"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          /><br />
          <button type="submit">Entrar</button>
          {error && <p style={{ color: "red" }}>{error}</p>}
        </form>
      )}
    </div>
  );
}
