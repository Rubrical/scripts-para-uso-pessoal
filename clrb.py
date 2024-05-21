import subprocess
import sys


def check_if_is_git_repository() -> None:
    """
    Irá verificar se o diretório atual é um repositório git.
    Raises:
        CalledProcessError
    """
    try:
        subprocess.run(["git", "rev-parse", "--is -inside-work-tree"],
                       check=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    except subprocess.CalledProcessError:
        print("Diretório atual não é um repositório git")
        sys.exit(1)


def check_if_git_is_installed() -> None:
    """
    Verifica se o git está instalado.
    Raises:
        CalledProcessError
    """
    try:
        subprocess.run(["git", "--version"],
                       check=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

    except subprocess.CalledProcessError:
        print("Git não instalado, instale-o!")
        sys.exit(1)


def change_branch(branch_name) -> None:
    """
    Muda para a branch especificada.

    Raises:
        CalledProcessError
    """
    try:
        subprocess.run(["git", "checkout", "-b", branch_name], check=True)
        print(f"Agora na branch '{branch_name}'.")
    except subprocess.CalledProcessError:
        print(f"Não foi possível altearar a branch para: '{branch_name}'.")
        sys.exit(1)


def command_help_or_documentation() -> str:
    """
    Documentação do comando help para o script.
    Returns:
        help_message -> str
    """
    help_message: str = "COMO USAR O SCRIPT:\n Uso: python change_local_repository_branch.py <funcionalidade> <CódigoCasoDeUso> <NomeCasoDeUso> <FuncionalidadeCasoDeUso>"
    return help_message


if __name__ == "__main__":
    message = command_help_or_documentation()

    try:
        if sys.argv[1] == "--help":
            print(message)
            sys.exit(1)

        if len(sys.argv) != 5:
            print(message)
            sys.exit(1)

        feature: str = sys.argv[1]
        uc_code: str = sys.argv[2]
        uc_name: str = sys.argv[3]
        funcionalite: str = sys.argv[4]

        print(f"{feature}/{uc_code}_{uc_name}_{funcionalite}")

        branch_name: str = f"{feature}/{uc_code}_{uc_name}_{funcionalite}"
    except IndexError:
        print(message)
        sys.exit(1)

    repeat: bool = True
    while repeat:
        confirm_input: str = str(input("Está correta a entrada? S/N\n"))

        if confirm_input.lower() == "s":
            repeat = False

            check_if_git_is_installed()
            check_if_is_git_repository()
            change_branch(branch_name)

            print('Tudo finlizado com sucesso!')

        elif confirm_input.lower() == "n":
            repeat = False
            print("Rode o script novamente com as mudanças devidas")
        else:
            print("Digite apenas S ou N")
