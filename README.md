# Master Thesis Project scripts and Evaluations store

## 1. ORB SLAM 2 with SC depth
- These observations are from using ORBSLAM2 with 12 scenes dataset.
- Depthmaps are generated with pretrained SC Depth model.
- SC Depth model is trained on indoor nyu2 dataset.

Individual Axis'             |  XY Trajectory
:-------------------------:|:-------------------------:
![](./orbslam_and_scdepth_performance_xyz.png) |  ![](./orbslam_and_scdepth_performance_traj.png)

EVO_APE Evaluation:

Max | Mean | Median | Min | RMSE | SSE | std
--- | ---  | ---    | --- |---   |---  |--- 
0.105639 | 0.054230 | 0.051419 | 0.010459 | 0.058585 | 1.692088 | 0.022165
