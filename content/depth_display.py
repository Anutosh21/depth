"""Display helpers only; the notebook supplies the PyTorch depth prediction."""
import numpy as np


def colorize_depth(depth):
    """Playground-style percentile scaling and Turbo colour lookup."""
    flat = np.asarray(depth, dtype=np.float32).reshape(-1)
    if not np.isfinite(flat).all():
        raise ValueError('Depth contains non-finite values')
    sample = np.sort(flat[::max(1, flat.size // 6000)])
    lo, hi = sample[int(sample.size * .01)], sample[int(sample.size * .99)]
    indices = np.rint(np.clip((depth - lo) / (hi - lo if hi > lo else 1), 0, 1) * 255).astype(np.uint8)
    x = np.arange(256, dtype=np.float64) / 255
    # Turbo polynomial (Mikhailov, 2019), also used by ExecuTorch's playground.
    red = .13572138 + x * (4.6153926 + x * (-42.66032258 + x * (132.13108234 + x * (-152.94239396 + x * 59.28637943))))
    green = .09140261 + x * (2.19418839 + x * (4.84296658 + x * (-14.18503333 + x * (4.27729857 + x * 2.82956604))))
    blue = .1066733 + x * (12.64194608 + x * (-60.58204836 + x * (110.36276771 + x * (-89.90310912 + x * 27.34824973))))
    palette = np.rint(np.clip(np.stack([red, green, blue], axis=1) * 255, 0, 255)).astype(np.uint8)
    return palette[indices], (float(lo), float(hi))
