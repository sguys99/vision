import torch
from einops import rearrange

# torch.Tensor : 클래스
# torch.tensor : 함수


# x = torch.randn(2, 4)

# y = rearrange(x, "group element -> (group element)")

# print(x[1][2] == y[6])

# -----------------------

# x = torch.randn(3, 2, 4)
# y = rearrange(x, "metagroup group element -> (metagroup group element)")

# print(x[1][1][2] == y[14])

# x = torch.randn(3, 2, 4)
# y = rearrange(x, "metagroup group element -> metagroup (group element)")

# print(x[1][1][2] == y[1][6])

# # -----------------------

# x = torch.randn(3, 2, 4)
# y = rearrange(x, "metagroup group element -> (metagroup group) element")

# print(x[1][1][2] == y[3][2])

# # einops 중
# x = torch.randn(8)
# y = rearrange(x, "(group element) -> group element", element = 4)

# print(x[6] == y[1][2])

# #----------------------
# x = torch.randn(8)
# y = rearrange(
#     x, 
#     "(metagroup group element) -> metagroup group element",
#     metagroup = 2,
#     group = 2,
#     )

# print(x[6] == y[1][1][0])

# # ----------------------

# x = torch.randn(3, 8)
# y = rearrange(
#     x,
#     "metagroup (group element) -> metagroup group element",
#     group = 2
# )

# print(x[1][5] == y[1][1][1])

# einops 하

# x = torch.randn(2, 4)
# y = rearrange(x, "group element -> element group")

# print(x[1][2] == y[2][1])

