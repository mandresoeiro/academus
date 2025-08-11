import Layout from "../features/layout/Layout";
import { useUser } from "../context/UserContext";
import { useNavigate } from "react-router-dom";
import { clearToken } from "../services/authService";

export default function Dashboard() {
  const { user, setUser } = useUser();
  const navigate = useNavigate();

  const handleLogout = () => {
    clearToken();
    setUser(null);
    navigate("/");
  };

  return (
    <Layout>
      <div className="bg-white p-6 rounded-xl shadow-lg max-w-2xl mx-auto">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-xl font-bold text-blue-700">🟦 Dashboard do Academus</h1>
          <button onClick={handleLogout} className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">Sair</button>
        </div>
        <p className="text-lg mb-2">Bem-vindo, <strong className="text-blue-800">{user}</strong>!</p>
        <p className="text-gray-700">Você está logado no sistema.<br />Em breve verá aqui tarefas, comentários e validações por setor. 🧠</p>
      </div>
    </Layout>
  );
}
