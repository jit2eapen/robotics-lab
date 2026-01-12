#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class TFListenerNode(Node):
    def __init__(self):
        super().__init__('tf_listener_node')

        # Declare a parameter to toggle rotation (Default is False)
        # You can change this to True when running the script
        self.declare_parameter('show_rotation', False)

        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.timer = self.create_timer(0.1, self.on_timer)

    def on_timer(self):
        # Fetch the current value of the parameter
        show_rotation = self.get_parameter('show_rotation').get_parameter_value().bool_value
        
        to_frame_rel = 'link5'
        from_frame_rel = 'link_base'

        try:
            t = self.tf_buffer.lookup_transform(from_frame_rel, to_frame_rel, rclpy.time.Time())

            # Coordinates
            x = t.transform.translation.x
            y = t.transform.translation.y
            z = t.transform.translation.z

            # Build the output string
            output = f"x = {x:.3f}, y = {y:.3f}, z = {z:.3f}"

            # Add rotation only if the parameter is set to True
            if show_rotation:
                rx = t.transform.rotation.x
                ry = t.transform.rotation.y
                rz = t.transform.rotation.z
                rw = t.transform.rotation.w
                output += f" | rx = {rx:.3f}, ry = {ry:.3f}, rz = {rz:.3f}, rw = {rw:.3f}"

            self.get_logger().info(output)

        except TransformException as ex:
            # Silently wait for the transform to become available
            pass

def main():
    rclpy.init()
    node = TFListenerNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
