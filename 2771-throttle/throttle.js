var throttle = function(fn, t) {
    let timer;      // interval 핸들
    let lastArgs;   // 마지막 인자
    let callCount;  // 창 내 호출 여부 추적

    return function(...args) {
        lastArgs = args;
        callCount = (callCount || 0) + 1;

        if (timer) return;              // 이미 창이 굴러가는 중이면 대기만

        // leading 실행
        fn(...lastArgs);
        callCount = 1;

        // 창 시작: trailing 후보가 있으면 창 끝마다 실행
        timer = setInterval(() => {
            if (callCount > 1) {
                // trailing: 창 동안 추가 호출이 있었다면 마지막 인자로 한 번 실행
                fn(...lastArgs);
                callCount = 1;          // 다음 창의 leading처럼 간주
            } else {
                // 추가 호출 없으면 종료
                clearInterval(timer);
                timer = null;
            }
        }, t);
    };
};
