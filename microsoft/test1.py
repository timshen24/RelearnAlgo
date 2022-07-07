# enum LogicalOperator {
#     And,
#     Or,
#     Not
# }
#
# enum ComputeOperator {
#
#     Equal,
#
#     NotEqual,
#
#     # GreaterThan,
# }
#
#
# class Node {
#     Node[] children;
# }
#
# class LogicalNode: Node {
#     LogicalOperator operator；
#     def __repr__():
#
# }
#
# class ComputeNode: Node
# {
#     string name;
#     ComputeOperator operator；
#     string value;
# }
#
# And
# | | |
# A = 1
# B = 2
# C = 3
#
# (A == 1) and (B == 2) and (C == 3)
#
#     And
#      |
# Not     | A < 2
#  |
# A = 1
#
# (Not(A == 1)) and (A < 2)
#
#     Or
# |     |
# A = 1  A = 2
#
#
# (A == 1) or (A == 2)
#
# res = ""
# def validateAndConvertTree(root: Node) -> Boolean:
#     global res
#     if not root:
#         return True
#     if not root.children and root.isinstanceof(ComputeNode):
#         res += str(root)
#         return True
#     if root.isinstanceof(LogicalNode):
#         for child in root.children:
#             if validateAndConvertTree(child):
#                 res += str(child)
#                 return True
#             else:
#                 return False
#     else:
#         return False
#
