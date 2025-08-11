import Layout from "../features/layout/Layout";

export default function TarefasPage() {
  const tarefas = [
    { id: 1, titulo: "Revisar apostila", setor: "docência", status: "pendente" },
    { id: 2, titulo: "Montar capa", setor: "comunicação", status: "em andamento" },
    { id: 3, titulo: "Checklist impressão", setor: "produção", status: "concluído" },
  ];

  return (
    <Layout>
      <div className="max-w-4xl mx-auto space-y-6">
        <h2 className="text-2xl font-bold text-blue-800">📋 Minhas Tarefas</h2>
        <div className="grid gap-4 grid-cols-1 sm:grid-cols-2">
          {tarefas.map((tarefa) => (
            <div key={tarefa.id} className="bg-white shadow-md rounded-lg p-4 border-l-4 border-blue-600">
              <h3 className="font-semibold text-lg text-gray-800">{tarefa.titulo}</h3>
              <p className="text-sm text-gray-500">Setor: {tarefa.setor}</p>
              <p className="text-sm mt-1 text-blue-700">Status: {tarefa.status}</p>
            </div>
          ))}
        </div>
      </div>
    </Layout>
  );
}
