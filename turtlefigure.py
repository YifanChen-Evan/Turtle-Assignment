from turtle import *
import math

# Binary tree
def tree(order, length, pen):
     if order == 0 or length < 2:
          return
     # endif
     pen.forward(length)
     pen.left(45)
     tree(order - 1, length / 2, pen)
     pen.right(90)
     tree(order - 1, length / 2, pen)
     pen.left(45)
     pen.backward(length)



# quad tree
def dandelion(order, length, pen):
     if order==0 or length<2 :
          return
     # endif
     pen.forward(length)
     pen.left(90)
     dandelion(order - 1, length / 2, pen)
     pen.right(60)
     dandelion(order - 1, length / 2, pen)
     pen.right(60)
     dandelion(order - 1, length / 2, pen)
     pen.right(60)
     dandelion(order - 1, length / 2, pen)
     pen.left(90)
     pen.backward(length)
#end




# Fern
def fern(order, length, pen):
     # termination
     if order==0 or length<2:
          return
     #endif
     pen.forward(2 * length / 3)
     pen.left(45); fern(order - 1, length / 2, pen);pen.right(45)
     pen.forward(2 * length / 3)
     pen.right(30);fern(order - 1, length / 2, pen);pen.left(30)
     pen.forward(2 * length / 3)
     pen.right(10);fern(order - 1, 0.75 * length, pen);pen.left(10)
     pen.backward(2 * length)
# end



# Koch
def koch(order, length, pen):
     if order==0 or length<2 :
          pen.forward(length)
          return
     #endif
     koch(order - 1, length / 3, pen)
     pen.left(60)
     koch(order - 1, length / 3, pen)
     pen.right(120)
     koch(order - 1, length / 3, pen)
     pen.left(60)
     koch(order - 1, length / 3, pen)
#end



# snow flake
def flake(order, length, pen):
     for i in range(3):
          koch(order, length, pen)
          pen.right(120)
     #endfor
#end



# antiflake
def antiflake(order, length, pen):
     for i in range(3):
          koch(order, length, pen)
          pen.left(120)
     #endfor
#end



# S-Gasket
def sgasket(order, length, pen):
     #termination
     if order==0 or length<2:
          return
     #endif
     for  i in range(3):
          sgasket(order - 1, length / 2, pen)
          pen.forward(length)
          pen.left(120)
#end



# Swiss-Gasket
def swiss(order, length, pen):
     #termination:
     if order==0 or length<2:
          return
     #endif
     for i in range(4):
          swiss(order - 1, length / 3, pen)
          pen.forward(length)
          pen.left(90)
#end



# Pentagon-Gasket
def pent(order, length, pen):
     #termination:
     if order==0 or length<2:
          return
     #endif
     for i in range(5):
          pent(order - 1, length * 0.381966601126, pen)
          pen.forward(length)
          pen.left(72)
#end



# Expanding-Pentagon
def expanding(order, length, pen):
     #termination:
     for order in range(length):
         pen.pensize(order/10 + 1)
         pen.forward(order)
         pen.left(59)
#end



# Chain-Circle
def chain(order, length, pen):
     #termination:
     if order==0 or length<2:
          return
     #endif
     for i in range(order):
          pen.down()
          pen.circle(length)
          pen.up()
          pen.forward(length)
#end
