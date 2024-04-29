from vuer import Vuer, VuerSession
from vuer.schemas import DefaultScene, Urdf

# app = Vuer()
app = Vuer(host='0.0.0.0', cert="", key="", queries=dict(grid=False))


@app.spawn(start=True)
async def main(session: VuerSession):
    app.set @ DefaultScene(Urdf("urdf/stompy/robot.urdf"))

    while True:
        await session.sleep(0.1)