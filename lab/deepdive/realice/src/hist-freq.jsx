
function wordFreq(text) {
  let freq = {};
  let words = text.matchAll(/[a-zA-Z']{2,}|[a-zA-Z]/g);
  for (let mat_x of words) {
    let w = mat_x[0]
    w = w.toUpperCase();

    if (w in freq) {
      freq[w] += 1;
    } else {
      freq[w] = 1;
    }
  }
  return freq;
}

export default function HistFreq({ rawText, onTargetUpdate }) {
  let freqDict = wordFreq(rawText);
  let freqHist = layoutFreq(freqDict, onTargetUpdate);

  function layoutFreq(freqDict, onTargetUpdate) {
    let sortedArr = Array.from(Object.entries(freqDict))
      .sort((a, b) => b[1] - a[1]);
    const freqSum = sortedArr
      .map((x) => x[1])
      .reduce((x, st) => st += x, 0);

    let hist = [];
    for (let [ch_x, freq_x] of sortedArr.slice(0, 20)) {
      const ratio = freq_x / freqSum * 100;
      let textContent = "";
      textContent = ch_x.padStart(5) + " ";
      textContent += `[${ratio.toFixed(2).padStart(5)}%] `;
      textContent += "#".repeat(~~(ratio / 0.1));
      let hist_elem = (
        <div
          className="hist-elem"
          key={`hist-elem-${ch_x}`}
          onMouseEnter={()=>onTargetUpdate(ch_x)}>{textContent}</div>
      );

      hist.push(hist_elem);
    }
    return hist;
  }


  return (
    <div id="alice-hist">{freqHist}</div>
  )
}