Space Group Operation
=====================

In this page, some formulations are provided used in this package.

.. contents::
   :depth: 2
   :local:

Space group operation
---------------------

Space group operation :math:`(\boldsymbol{W}, \boldsymbol{w})`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A symmetry operation consists of a pair of the rotation part
:math:`\boldsymbol{W}` and translation part :math:`\boldsymbol{w}`,
and is represented as :math:`(\boldsymbol{W}, \boldsymbol{w})` in the
dichlib document. The symmetry operation transfers :math:`\boldsymbol{x}` to
:math:`\tilde{\boldsymbol{x}}` as follows:

.. math::
   :label: space_group_operation

   \tilde{\boldsymbol{x}} = \boldsymbol{W}\boldsymbol{x} + \boldsymbol{w}.



Separating :math:`\boldsymbol{w}_{intr}` and :math:`\boldsymbol{w}_{loc}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Translation part of space group operation :math:`\boldsymbol{w})` can be
separate its intrinsic part and location part as follows:

.. math::
   :label: separating_translation_part

   \boldsymbol{w} = \boldsymbol{w}_{intr} + \boldsymbol{w}_{loc}

In order to determine the intrinsic part :math:`\boldsymbol{w}_{intr}`,
the index :math:`k` of the space group operation :math:`(\boldsymbol{W}, \boldsymbol{w})`
is determined. :math:`k` is defined as the minumum positive integer which fullfil
the next equation:

.. math::

   (\boldsymbol{W}, \boldsymbol{w})^k = (\boldsymbol{I}, \boldsymbol{t}).

Then, :math:`\boldsymbol{w}_{intr}` is determined as follows:

.. math::

  \boldsymbol{w}_{intr} = \boldsymbol{t} / k



Geometric element of space group operation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Geometric element of the space group operation :math:`\boldsymbol{x}_{ele}`
is determined as follows:

.. math::

   \boldsymbol{W}\boldsymbol{x}_{ele} + \boldsymbol{w}_{loc} = \boldsymbol{x}_{ele}
