(function () {
    const videoElement = document.querySelector('video');

    function hideControlsInstantly() {
        const controlBar = document.querySelector('.ytp-chrome-bottom');
        const progressBar = document.querySelector('.ytp-chrome-top');
        const gradientTop = document.querySelector('.ytp-gradient-top');
        const branding = document.querySelectorAll(".ytp-iv-player-content");

        if (controlBar) controlBar.style.display = 'none';
        if (progressBar) progressBar.style.display = 'none';
        if (gradientTop) gradientTop.style.display = 'none';
        if (branding) branding.forEach(e => e.style.display = 'none');

        const overlayControls = document.querySelector('.ytp-gradient-bottom');
        if (overlayControls) overlayControls.style.display = 'none';
    }
    hideControlsInstantly()
    let overlay = document.getElementById('video-overlay');

    if (!overlay) {
        const url = new URL(window.location.href);
        const timeParam = url.searchParams.get("t");
        let currentTime = videoElement.currentTime;
        videoElement.volume = 1;
        if (timeParam) {
            const videoTime = parseInt(timeParam, 10);
            videoElement.currentTime = videoTime;
            currentTime = videoTime;
            videoElement.pause();
        } else {
            url.searchParams.set("t", Math.floor(videoElement.currentTime));
            window.history.replaceState({}, '', url.toString());
        }

        addEventListener("keyup",
            (event) => {
                if (event.code == "KeyS") {
                    videoElement.currentTime = currentTime;
                    videoElement.pause();
                }
            }
        );
        const videoTitle = document.querySelector('div#title yt-formatted-string').textContent;
        const channelName = document.querySelector('ytd-channel-name a').textContent;
        const avatarImgUrl = document.querySelector('ytd-video-owner-renderer img').src;
        overlay = document.createElement('div');
        overlay.id = 'video-overlay';
        overlay.style.position = 'absolute';
        overlay.style.bottom = '10px';
        overlay.style.right = '10px';
        overlay.style.color = 'white';
        overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.7)';
        overlay.style.padding = '10px';
        overlay.style.borderRadius = '5px';
        overlay.style.zIndex = '9999';
        overlay.style.fontSize = '16px';
        overlay.style.display = 'flex';
        overlay.style.alignItems = 'center';

        overlay.setAttribute('data-time', currentTime);

        /*const textContainer = document.createElement('div');
        const titleElement = document.createElement('strong');
        titleElement.textContent = videoTitle;

        const channelElement = document.createElement('div');
        channelElement.textContent = channelName;

        textContainer.appendChild(titleElement);
        textContainer.appendChild(document.createElement('br'));
        textContainer.appendChild(channelElement);

        const avatarImg = document.createElement('img');
        avatarImg.src = avatarImgUrl;
        avatarImg.style.width = '40px';
        avatarImg.style.height = '40px';
        avatarImg.style.marginLeft = '10px';

        overlay.appendChild(textContainer);
        overlay.appendChild(avatarImg);*/

        const videoContainer = document.querySelector('div.ytp-caption-window-container');
        videoContainer.appendChild(overlay);
    }
})();


