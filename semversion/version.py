class Version:
    DEFAULT_VERSION = "0.0.1"
    FILE_PATH = ".version"

    MAJOR = 0
    MINOR = 1
    PATCH = 2

    @staticmethod
    def get():
        try:
            with open(Version.FILE_PATH, "r") as version_file:
                return version_file.read().strip()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The {Version.FILE_PATH} file was not found. Please create the file with the version number."
            )

    @staticmethod
    def _write_version(new_version):
        with open(Version.FILE_PATH, "w") as version_file:
            version_file.write(new_version)

    @staticmethod
    def increment(part):
        try:
            current_version = Version.get()
            components = list(map(int, current_version.split(".")))

            if part == Version.MAJOR:
                components[Version.MAJOR] += 1
                components[Version.MINOR] = 0
                components[Version.PATCH] = 0
            elif part == Version.MINOR:
                components[Version.MINOR] += 1
                components[Version.PATCH] = 0
            elif part == Version.PATCH:
                components[Version.PATCH] += 1

            new_version = ".".join(map(str, components))
            Version._write_version(new_version)
            return new_version
        except FileNotFoundError:
            raise FileNotFoundError(
                f"The {Version.FILE_PATH} file was not found. Please create the file with the version number."
            )

    @staticmethod
    def initialize():
        with open(Version.FILE_PATH, "w") as version_file:
            version_file.write(Version.DEFAULT_VERSION)
