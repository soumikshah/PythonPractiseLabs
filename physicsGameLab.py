from direct.showbase.ShowBase import ShowBase
from direct.showbase.InputStateGlobal import inputState

from panda3d.core import Vec3
from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import BulletSphereShape
from panda3d.bullet import BulletDebugNode


class BouncingBall(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        base.disableMouse()
        base.camera.setPos(0, -200, 10)

        # create bullet world
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))

        # setup room
        self.setupRoom()
        # setup character`
        self.setupCharacter()
        self.turnOnDegubMode()
        inputState.watchWithModifiers('forward', 'w')
        inputState.watchWithModifiers('left', 'a')
        inputState.watchWithModifiers('reverse', 's')
        inputState.watchWithModifiers('right', 'd')
        inputState.watchWithModifiers('turnLeft', 'q')
        inputState.watchWithModifiers('turnRight', 'e')

        taskMgr.add(self.update, 'update')

    # Update
    def update(self, task):
        self.processInput()
        dt = globalClock.getDt()
        self.world.doPhysics(dt, 10, 1/180.0)
        return task.cont

    def turnOnDegubMode(self):
        debugNode = BulletDebugNode('Debug')
        debugNode.showWireframe(True)
        debugNode.showConstraints(True)
        debugNode.showBoundingBoxes(False)
        debugNode.showNormals(False)
        debugNP = render.attachNewNode(debugNode)
        debugNP.show()
        self.world.setDebugNode(debugNP.node())

    def processInput(self):
        force = Vec3(0, 0, 0)
        torque = Vec3(0, 0, 0)

        if inputState.isSet('forward'): force.setY( 1.0)
        if inputState.isSet('reverse'): force.setY(-1.0)
        if inputState.isSet('left'):    force.setX(-1.0)
        if inputState.isSet('right'):   force.setX( 1.0)
        if inputState.isSet('turnLeft'):  torque.setZ( 1.0)
        if inputState.isSet('turnRight'): torque.setZ(-1.0)

        force *= 60.0
        torque *= 4.0

        self.sphere.node().setActive(True)
        self.sphere.node().applyCentralForce(force)
        self.sphere.node().applyTorque(torque)

    def setupRoom(self):
        # Floor
        floorShape = BulletPlaneShape(Vec3(0, 0, 1), 0)
        floorNode = BulletRigidBodyNode('Floor')
        floorNode.addShape(floorShape)
        floorNodePath = self.render.attachNewNode(floorNode)
        floorNodePath.setPos(0, 0, 0)
        self.world.attachRigidBody(floorNode)
        floorModel = self.loader.loadModel("models/misc/rgbCube")
        floorModel.setScale(100, 100, 1)
        floorModel.setPos(0, 0, 0)
        floorModel.reparentTo(self.render)

        # Right Wall
        floorShape = BulletPlaneShape(Vec3(-1, 0, 0), 0)
        floorNode = BulletRigidBodyNode('Floor')
        floorNode.addShape(floorShape)
        floorNodePath = self.render.attachNewNode(floorNode)
        floorNodePath.setPos(50, 0, 0)
        self.world.attachRigidBody(floorNode)
        floorModel = self.loader.loadModel("models/misc/rgbCube")
        floorModel.setScale(1, 100, 150)
        floorModel.setPos(50, 0, 75)
        floorModel.reparentTo(self.render)

        # Left Wall
        floorShape = BulletPlaneShape(Vec3(1, 0, 0), 0)
        floorNode = BulletRigidBodyNode('Floor')
        floorNode.addShape(floorShape)
        floorNodePath = self.render.attachNewNode(floorNode)
        floorNodePath.setPos(-50, 0, 0)
        self.world.attachRigidBody(floorNode)
        floorModel = self.loader.loadModel("models/misc/rgbCube")
        floorModel.setScale(1, 100, 150)
        floorModel.setPos(-50, 0, 75)
        floorModel.reparentTo(self.render)

    def setupCharacter(self):
        # Sphere
        shape = BulletSphereShape(2)
        node = BulletRigidBodyNode('Box')
        node.setMass(10.0)
        node.addShape(shape)
        self.sphere = self.render.attachNewNode(node)
        self.sphere.setPos(0, 10, 150)
        self.world.attachRigidBody(node)

        smileyFace = self.loader.loadModel("models/panda")
        smileyFace.reparentTo(self.sphere)
        smileyFace.setScale(2)

simulation = BouncingBall()
simulation.run()
