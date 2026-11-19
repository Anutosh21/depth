# Let's give our camera some depth

Try the included photo, upload your own or turn on your camera. Compare the
original with a coloured depth map using the slider or side-by-side view.
Everything runs in your browser.

- [Open the WebGPU notebook](https://anutosh21.github.io/depth/lab/index.html?path=depth-webgpu.ipynb)
- [Open the CPU notebook](https://anutosh21.github.io/depth/lab/index.html?path=depth-cpu.ipynb)

Run the cells from top to bottom in a fresh kernel, then click **Start camera** and
allow access. Run one notebook at a time when comparing CPU and WebGPU. The model
predicts relative depth, not distances in metres.

The original pretrained weights (about 95 MiB), model code and sample photo are
included in `content/`. Both notebooks load the included weights directly.

Shoutout to [Depth Anything V2](https://github.com/DepthAnything/Depth-Anything-V2)
and [ExecuTorch's depth demo](https://executorch.ai/playground/webgpu/#/demo/depth)
for the inspiration! Built from the
[Xeus-Lite template](https://github.com/jupyterlite/xeus-lite-demo).

Model and weights: Depth Anything V2 Small, Apache-2.0. Photo: Elf; derivatives by
Djmirko and FT2, CC BY-SA 3.0. Displayed photo derivatives retain that license.
Licensing and source details are in `content/LICENSE-Depth-Anything-V2` and
`content/sources.json`.

To deploy, set **Settings → Pages → Source → GitHub Actions**, then push to `main`.
