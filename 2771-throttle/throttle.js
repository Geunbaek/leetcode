var throttle = function (fn, t) {
  let last = 0;              // 마지막 실행 시각
  let timeout = null;        // 예약된 trailing 타이머
  let pendingArgs = null;    // trailing용 최신 인자
  let pendingThis = null;    // trailing용 최신 this

  return function (...args) {
    const now = Date.now();
    const remaining = t - (now - last);

    if (remaining <= 0) {
      // 창이 지났으므로 즉시 실행 (leading)
      if (timeout) {
        clearTimeout(timeout);
        timeout = null;
      }
      last = now;
      fn.apply(this, args);
    } else {
      // 창 안이므로 trailing 예약/업데이트
      pendingArgs = args;
      pendingThis = this;
      if (!timeout) {
        timeout = setTimeout(() => {
          timeout = null;
          last = Date.now();
          fn.apply(pendingThis, pendingArgs);
          pendingArgs = pendingThis = null;
        }, remaining);
      }
    }
  };
};
