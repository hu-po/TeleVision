from asyncio import sleep

from vuer import Vuer, VuerSession
from vuer.schemas import Scene, Urdf, Movable, PointLight, AmbientLight

from stompy_poses import *

pi = 3.1415

app = Vuer(static_root="/home/oop/dev/TeleVision/urdf/stompy_tiny")

@app.spawn(start=True)
async def main(app: VuerSession):
    # Note: you can only use `set` operator with Scene objects. This is a special operator.
    app.set @ Scene(
        rawChildren=[
            AmbientLight(intensity=1),
            Movable(PointLight(intensity=1), position=[0, 0, 2]),
            Movable(PointLight(intensity=3), position=[0, 1, 2]),
        ],
        grid=True,
        up=[0, 0, 1]
    )
    await sleep(0.1)

    i = 0
    while True:

        pose = FULL_ZERO_POSE
        pose.update(RIGHT_ARM_READY_TO_MANIP)
        pose.update(LEFT_ARM_READY_TO_MANIP)
        pose.update(HEAD_LOOK_FORWARD)

        app.upsert @ Urdf(
            src="http://localhost:8012/static/robot.urdf",
            jointValues=pose,
            position=[0, 0, 0.295],
            key="robot",
        )
        await sleep(0.016)
        i += 1