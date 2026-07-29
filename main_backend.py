

def text_deployer():
    text = """


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse semper turpis sed lectus malesuada gravida. Quisque maximus ante arcu, eu scelerisque lorem tempor id. Cras eleifend, turpis quis finibus auctor, turpis lacus egestas nibh, quis luctus sem turpis mollis tortor. Integer hendrerit dapibus est, eu porta diam fringilla quis. Etiam pulvinar commodo diam, eu tempus nisi ultricies ac. Integer in eleifend libero. Nulla ac metus in massa condimentum consequat vestibulum id est. Cras ac metus odio. Sed condimentum tempus ultricies. Sed dignissim consectetur est vitae luctus. Curabitur vel mollis eros. Pellentesque est augue, mattis sit amet euismod viverra, blandit sed metus. Nulla pulvinar ex porttitor risus congue congue. Sed est justo, rhoncus et elit eu, dignissim porta mi. Morbi convallis, dui id posuere porttitor, eros nisi volutpat enim, eu scelerisque erat sem in lorem.

Duis gravida ante vel iaculis pellentesque. Suspendisse eget efficitur risus. Vivamus in molestie mi. Nam semper volutpat faucibus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In quis ante ultricies, facilisis est ut, laoreet lectus. Vivamus et nisl quis justo aliquam faucibus. Praesent risus neque, finibus vulputate pellentesque ut, volutpat ut quam. Proin tristique neque ut mi convallis tincidunt. Fusce arcu justo, pharetra et mauris sit amet, eleifend convallis neque. In hac habitasse platea dictumst. Pellentesque diam tortor, mollis nec nisl ut, vulputate malesuada purus. Mauris in orci sodales, finibus felis at, eleifend dui. Etiam ligula neque, facilisis pharetra luctus at, vulputate eget velit.

Suspendisse lacinia massa vel justo tincidunt ultricies. Duis eget tincidunt velit. Vestibulum rutrum sollicitudin eros. Curabitur eget urna eget risus pretium sodales. Sed dui erat, fringilla hendrerit pretium vulputate, fermentum et libero. Curabitur tempus est id justo vehicula, in vulputate mi posuere. Integer interdum sapien sed porta tempor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent ut lacus faucibus, rhoncus mi et, lobortis ante.

Vivamus ultrices lectus vel egestas convallis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Donec id dapibus dui. Praesent viverra et leo vitae pulvinar. Duis eleifend lacinia ex, a efficitur lacus tempor sit amet. Curabitur dui sapien, cursus eget eros id, facilisis volutpat arcu. Donec in justo ut lorem tempus gravida nec ut odio. Fusce eu scelerisque ipsum. Proin nibh ipsum, blandit sollicitudin tempor et, egestas eget erat. In auctor lacus quam, et euismod augue aliquam ac. Morbi commodo vel nulla eget tempus.

Curabitur ullamcorper porttitor mauris, viverra posuere ex sodales et. Aliquam erat volutpat. Sed luctus lorem sit amet orci volutpat, tincidunt placerat dolor tristique. Proin vehicula nibh a consequat vehicula. Phasellus a tortor erat. Nunc nec consectetur felis. Curabitur efficitur, diam eget convallis aliquet, leo lectus convallis purus, ac sagittis urna ligula ut massa. Suspendisse at ante eget odio porta facilisis. In et erat elementum, interdum nisl sit amet, lobortis arcu. Nunc tempus nunc eu sapien bibendum placerat. Integer et felis mollis, tincidunt tellus non, tempus nunc. Etiam non elit et felis laoreet vulputate eget non quam. Praesent dui velit, consequat sit amet nisl nec, hendrerit rutrum massa. 
"""
    splitted = text.split(".")
    enum = [f"{n:2d} {text}" for n, text in enumerate(splitted)]

    return enum
