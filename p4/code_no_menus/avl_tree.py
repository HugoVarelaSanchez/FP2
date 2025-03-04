# -*- coding: utf-8 -*-
# Copyright 2019, Profesorado de Fundamentos de Programación II
#                 Grado en Ciencia e Ingeneiría de Datos
#                 Facultade de Informática
#                 Universidade da Coruña
# based on:
# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from binary_search_tree import BST

def preorder_indent_BST(T, p, d):
        """Print preorder representation of a binary subtree of T rooted at p at depth d.
           To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
        if p is not None:
            # use depth for indentation
            print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
            preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
            preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1


class AVL(BST):
  """Sorted map implementation using an AVL tree."""
            

  #-------------------------- nested _Node class --------------------------
  class _Node(BST._Node):
    """Node class for AVL maintains height value for balancing.

    We use convention that a "None" child has height 0, thus a leaf has height 1.
    """
    __slots__ = '_height'         # additional data member to store height

    def __init__(self, element, parent=None, left=None, right=None):
      super().__init__(element, parent, left, right)
      self._height = 0            # will be recomputed during balancing
      
    def left_height(self):
      return self._left._height if self._left is not None else 0

    def right_height(self):
      return self._right._height if self._right is not None else 0

  #------------------------- positional-based utility methods -------------------------
  def _recompute_height(self, p):
    p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

  def _isbalanced(self, p):
    return abs(p._node.left_height() - p._node.right_height()) <= 1

  def _tall_child(self, p, favorleft=False): # parameter controls tiebreaker
    if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
      return self.left(p)
    else:
      return self.right(p)

  def _tall_grandchild(self, p):
    child = self._tall_child(p)
    # if child is on left, favor left grandchild; else favor right grandchild
    alignment = (child == self.left(p))
    return self._tall_child(child, alignment)

  def _rebalance(self, p):
    while p is not None:
      old_height = p._node._height                          # trivially 0 if new node
      if not self._isbalanced(p):                           # imbalance detected!
        # perform trinode restructuring, setting p to resulting root,
        # and recompute new local heights after the restructuring
        p = self._restructure(self._tall_grandchild(p))
        self._recompute_height(self.left(p))                
        self._recompute_height(self.right(p))                           
      self._recompute_height(p)                             # adjust for recent changes
      if p._node._height == old_height:                     # has height changed?
        p = None                                            # no further changes needed
      else:
        p = self.parent(p)                                  # repeat with parent

  #---------------------------- override balancing hooks ----------------------------
  def _rebalance_insert(self, p):
    self._rebalance(p)

  def _rebalance_delete(self, p):
    self._rebalance(p)

if __name__ == '__main__':
    # Solo para mostrar el funcionamiento de un BST. NO es un test exhaustivo

    def preorder_indent_BST(T, p, d):
        """Print preorder representation of a binary subtree of T rooted at p at depth d.
           To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
        if p is not None:
            # use depth for indentation
            print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
            preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
            preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1
            
    def preorder_indent_BST_alt(T, p, d):
        """Alternative version of preorder_indent_BST using iterator T.children().
        Print preorder representation of subtree of T rooted at p at depth d."""
        # use depth for indentation
        if p is not None:
            print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
            for c in T.children(p):
              preorder_indent_BST(T, c, d+1) # child depth is d+1
    


              
    print("Insertamos las claves en orden")
    tree = AVL()
    print("Árbol vacío"); preorder_indent_BST(tree,tree.root(),0)
    print("Insertamos 1"); tree[1] = 'A'; preorder_indent_BST(tree,tree.root(),0)
    print("Insertamos 2"); tree[2] = 'B'; preorder_indent_BST(tree,tree.root(),0)
    print("Insertamos 3"); tree[3] = 'C'; preorder_indent_BST(tree,tree.root(),0)
    print("Insertamos 4"); tree[4] = 'D'; preorder_indent_BST(tree,tree.root(),0)
    print("Insertamos 5"); tree[5] = 'E'; preorder_indent_BST(tree,tree.root(),0)
    print("Insertamos 6"); tree[6] = 'F'; preorder_indent_BST(tree,tree.root(),0)
    print("Insertamos 7"); tree[7] = 'G'; preorder_indent_BST(tree,tree.root(),0)
    
    clave_valor = tree.find_min()
    print("La clave menor del árbol es "+ str(clave_valor[0]) + " con valor " + str(clave_valor[1]))
    clave_valor = tree.find_max()
    print("La clave mayor del árbol es "+ str(clave_valor[0]) + " con valor " + str(clave_valor[1]))
 
    clave = 5.5
    clave_valor = tree.find_le(clave)
    print("La primera clave menor o igual que " + str(clave) + " es " + str(clave_valor[0]) + " con valor " + str(clave_valor[1]))
    clave_valor = tree.find_ge(clave)
    print("La primera clave mayor o igual que " + str(clave) + " es " + str(clave_valor[0]) + " con valor " + str(clave_valor[1]))
    
    clave = 5
    clave_valor = tree.find_lt(clave)
    print("La primera clave estrictamente menor que " + str(clave) + " es " + str(clave_valor[0]) + " con valor " + str(clave_valor[1]))
    clave_valor = tree.find_gt(clave)
    print("La primera clave estrictamente mayor que " + str(clave) + " es " + str(clave_valor[0]) + " con valor " + str(clave_valor[1]))
    
    clave_min, clave_max = 2, 6
    print("las claves entre " + str(clave_min) + " y " + str(clave_max) + " son: ", end="")
    for par in tree.find_range(clave_min, clave_max):
        print(par[0], end=" ")
    print()
    
    print("borramos la clave 1")
    del tree[1]
    preorder_indent_BST(tree,tree.root(),0)
    
    print("borramos la clave 2")
    del tree[2]
    preorder_indent_BST(tree,tree.root(),0)
    
    print("borramos la clave 3")
    del tree[3]
    preorder_indent_BST(tree,tree.root(),0)