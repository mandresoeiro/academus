import typer

app = typer.Typer(help="Academus CLI - Automação e IA")


@app.command()
def generate(
    prompt: str,
    tipo: str = typer.Option(
        "view", help="Tipo de recurso: view, model, serializer, template"
    ),
):
    """
    Gera um código com base em um prompt e tipo (simulado).
    """
    result = f"# Código gerado para tipo '{tipo}'\n\nprint('Executando: {prompt}')"
    typer.echo(result)


@app.command()
def audit(code: str):
    """
    Faz uma análise simulada do código enviado.
    """
    feedback = f"Análise: código parece válido. Trecho inicial: {code[:30]}..."
    typer.echo(feedback)


if __name__ == "__main__":
    app()
