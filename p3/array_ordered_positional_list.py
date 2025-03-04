# -*- coding: utf-8 -*-

# Copyright 2019, Profesorado de Fundamentos de Programación II
#                 Grado en Ciencia e Ingenería de Datos
#                 Facultade de Informática
#                 Universidade da Coruña
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

class ArrayOrderedPositionalList:
  """An array-based implementation of a sequential container of elements allowing positional access."""

  def __init__(self):
    """Create an empty list."""
    self._data = []

  #------------------------------- accessors -------------------------------
  def first(self):
    """Return the first Position in the list (or None if list is empty)."""
    if self.is_empty():
        return None
    else:
        return 0
    
  def last(self):
    """Return the last Position in the list (or None if list is empty)."""
    if self.is_empty():
        return None
    else:
        return len(self._data) - 1

  def before(self, p):
    """Return the Position just before Position p (or None if p is first)."""
    if 0 < p < len(self._data):
        return p-1
    elif p == 0:
        return None
    else:
        raise IndexError('p is not a valid position')
    

  def after(self, p):
    """Return the Position just after Position p (or None if p is last)."""
    if 0 <= p < (len(self._data) - 1):
        return p+1
    elif p == (len(self._data) - 1):
        return None
    else:
        raise IndexError('p is not a valid position')

  def __len__(self):
    """Return the number of elements in the list."""
    return len(self._data)

  def is_empty(self):
    """Return True if the list is empty."""
    return (len(self._data)) == 0

  def __iter__(self):
    """Generate a forward iteration of the elements of the list."""
    return iter(self._data)

# Otra opción más procedimental
#  def __iter__(self):
#    """Generate a forward iteration of the elements of the list."""
#    cursor = self.first()
#    while cursor is not None:
#      yield self.get_element(cursor)
#      cursor = self.after(cursor)
    
  def get_element(self, p):
    """Return the Element at position p of the list."""
    if 0 <= p < len(self._data):
        return self._data[p]
    else:
        raise IndexError('p is not a valid position')

  #------------------------------- mutators -------------------------------
  
  def add(self, e):
    """Insert element e into list and return new Position."""
    if self.is_empty() or e > self._data[len(self._data) - 1]:
        self._data.append(e)
        return len(self._data) - 1
    else:
        self._data.append(None)  # increase the suze of data
        p = len(self._data) - 2
        while p >= 0 and self._data[p] >= e:
            self._data[p + 1] = self._data[p]
            p -= 1
        self._data[p + 1] = e 
        return p + 1
    
#  def add(self, e):
#    """Insert element e into list and return new Position."""
#    if self.is_empty() or e > self._data[len(self._data) - 1]:
#        self._data.append(e)
#        return len(self._data) - 1
#    else:
#        p = len(self._data) - 1
#        while p >= 0 and self._data[p] >= e:
#            p -= 1
#        return self._data.insert(p + 1, e) 
#        return p + 1

  def delete(self, p):
    """Remove and return the element at Position p."""
    return self._data.pop(p)   # if p is not valid, it raises an exception

  def replace(self, p, e):
    """Replace the element at Position p with e.

    Return the element formerly at Position p.
    """
    old_value = self._data[p] # if p is not valid, it raises an exception
    self._data[p] = e
    return old_value
