# Resizing WSL disk

1. Shutdown WSL2
2. Use diskpart to update the size of the VHD found in `%LOCALAPPDATA%\Packages\<Distro>\LocalState`
3. Start WSL2
4. Use resize2fs to make WSL2 aware of the change
5. Restart WSL2

[Documentation](https://docs.microsoft.com/en-us/windows/wsl/compare-versions#expanding-the-size-of-your-wsl-2-virtual-hardware-disk)
