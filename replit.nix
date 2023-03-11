{ pkgs }: {
    deps = [
        pkgs.chromium
        pkgs.python39Packages.pip
        pkgs.chromedriver
        pkgs.python39Full
    ];
}