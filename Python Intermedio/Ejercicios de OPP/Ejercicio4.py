
class Head:
    def __init__(self, face, ears, hair, neck):
        self.face = face
        self.ears = ears
        self.hair = hair
        self.neck = neck


class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg ):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        

class Arm:
    def __init__(self, hand, wrist, forehand, elbow, shoulder):
        self.hand = hand
        self.wrist = wrist
        self.forehand = forehand
        self.elbow = elbow
        self.shoulder = shoulder
        

class Hand:
    def __init__(self, fingers, palm):
        self.fingers = fingers
        self.palm = palm
        

class Leg:
    def __init__(self, foot, ankle, calf, knee, thigh, hip):
        self.foot = foot
        self.ankle = ankle
        self.calf = calf
        self.knee = knee
        self.thigh = thigh
        self.hip = hip
        

class Feet:
    def __init__(self, toes, sole):
        self.toes = toes
        self.sole = sole
        

class Human:
    def __init__(self,torso):

        self.torso = torso


head = Head("face", "ears", "hair", "neck")

right_hand = Hand("right fingers", "right palm")
left_hand = Hand("left fingers", "left palm")

right_arm = Arm(right_hand, "right wrist", "right forearm", "right elbow", "right shoulder")
left_arm = Arm(left_hand, "left wrist", "left forearm", "left elbow", "left shoulder")

right_foot = Feet("right toes", "right sole")
left_foot = Feet("left toes", "left sole")

right_leg = Leg(right_foot, "right ankle", "right calf", "right knee", "right thigh", "right hip")
left_leg = Leg(left_foot, "left ankle", "left calf", "left knee", "left thigh", "left hip")

torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

body = Human(torso)

print(f"Human has a Head: {body.torso.head.face}")
print(f"Human has Arms: {body.torso.right_arm.forehand}, and, {body.torso.left_arm.forehand}")
print(f"Arms have Hands: {body.torso.right_arm.hand.fingers}, and, {body.torso.left_arm.hand.fingers}")
print(f"Human has Legs: {body.torso.right_leg.thigh}, and, {body.torso.left_leg.thigh}")
print(f"Legs have Feet: {body.torso.right_leg.foot.toes}, and, {body.torso.left_leg.foot.toes}")
print(f"Torso connects the Head, Arms, and Legs.")
