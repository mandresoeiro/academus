import { Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import { useUser } from "./context/UserContext";

function ProtectedRoute({ children }) {
  const { user } = useUser();
  return user ? children : <Navigate to="/" />;
}

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<LoginPage />} />
      <Route path="/dashboard" element={
        <ProtectedRoute>
          <Dashboard />
        </ProtectedRoute>
      } />
    </Routes>
  );
}
