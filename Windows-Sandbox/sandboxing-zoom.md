# Running a Video Conferencing software (Zoom) in Windows Sandbox

1. Make sure Virtualization is enabled in your BIOS.
2. Enable Windows Sandbox: `dism /online /Enable-Feature /FeatureName:"Containers-DisposableClientVM" -All`
3. Reboot when prompted.
4. Create `with-video.wsb` with the contents:
```xml
<Configuration>
   <VGpu>Enable</VGpu>
   <Networking>Enable</Networking>
   <AudioInput>Enable</AudioInput>
   <VideoInput>Enable</VideoInput>
</Configuration
```
5. Using explorer, open the above file.
6. In the sandbox, open a browser to [https://zoom.us/](https://zoom.us/)

[Documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-overview)
