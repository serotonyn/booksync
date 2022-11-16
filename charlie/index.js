export const getMapJson = (data) => {
  const smil = data.fragments.reduce(
    (acc, cur) => ((acc[cur.id] = cur), acc),
    {}
  );

  const spans = document.querySelectorAll(".span_");
  const audio = document.querySelector("audio");

  spans.forEach((s) => {
    s.addEventListener("click", (event) => {
      const begin = smil[event.target.id].begin;
      audio.currentTime = begin;
      audio.play();
    });
  });

  document.addEventListener("keydown", (ev) => {
    if (ev.code === "Enter") {
      audio.paused ? audio.play() : audio.pause();
    }
  });
};
