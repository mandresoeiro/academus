import { NavLink } from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="bg-blue-900 text-white w-64 h-screen p-4 flex flex-col">
      <h2 className="text-2xl font-bold mb-6">📘 Academus</h2>
      <nav className="flex flex-col gap-3">
        <NavLink to="/dashboard" className={({ isActive }) =>
          isActive ? "text-yellow-300 font-semibold" : "hover:text-yellow-200"}>🏠 Dashboard</NavLink>
        <NavLink to="/tarefas" className={({ isActive }) =>
          isActive ? "text-yellow-300 font-semibold" : "hover:text-yellow-200"}>📋 Tarefas</NavLink>
        <NavLink to="/comentarios" className={({ isActive }) =>
          isActive ? "text-yellow-300 font-semibold" : "hover:text-yellow-200"}>💬 Comentários</NavLink>
        <NavLink to="/validacoes" className={({ isActive }) =>
          isActive ? "text-yellow-300 font-semibold" : "hover:text-yellow-200"}>✅ Validações</NavLink>
      </nav>
    </div>
  );
}
