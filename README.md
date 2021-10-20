# Master Thesis Project scripts and Evaluations store

## 1. ORB SLAM 2 with SC depth
- These observations are from using ORBSLAM2 with 12 scenes dataset.
- Depthmaps are generated with pretrained SC Depth model.
- SC Depth model is trained on indoor nyu2 dataset.

## Living Room Split 1

Individual Axis'             |  XY Trajectory
:-------------------------:|:-------------------------:
![](./orbslam_and_scdepth_performance_xyz.png) |  ![](./orbslam_and_scdepth_performance_traj.png)

EVO_APE Evaluation:

Max | Mean | Median | Min | RMSE | SSE | std
--- | ---  | ---    | --- |---   |---  |--- 
0.105639 | 0.054230 | 0.051419 | 0.010459 | 0.058585 | 1.692088 | 0.022165

## Living Room Split 2 (506 frames)


Individual Axis'             |  XY Trajectory
:-------------------------:|:-------------------------:
![](./orbslam_and_scdepth_performance_xyz_1.png) |  ![](./orbslam_and_scdepth_performance_traj_1.png)

EVO_APE Evaluation:

Max | Mean | Median | Min | RMSE | SSE | std
--- | ---  | ---    | --- |---   |---  |--- 
0.148238 | 0.068421 | 0.065743 | 0.010298 | 0.074746 | 2.826994 | 0.030092

## Living Room Split 3 (529 frames)

Individual Axis'             |  XY Trajectory
:-------------------------:|:-------------------------:
![](./orbslam_and_scdepth_performance_xyz.png) |  ![](./orbslam_and_scdepth_performance_traj.png)

EVO_APE Evaluation:

Max | Mean | Median | Min | RMSE | SSE | std
--- | ---  | ---    | --- |---   |---  |--- 
0.105639 | 0.054230 | 0.051419 | 0.010459 | 0.058585 | 1.692088 | 0.022165
