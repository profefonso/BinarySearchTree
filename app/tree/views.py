from tree.models import Tree
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from tree.serializers.tree import TreeSerializer
from rest_framework.response import Response

from .function.binary import BinarySearchTree, InPreOrder


# This class is a view show all Tree's
class TreeList(generics.ListCreateAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    name = 'tree-list'


# This class is a view show details of one tree
class TreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tree.objects.all()
    serializer_class = TreeSerializer
    name = 'tree-detail'


# This class is a view ordered tree in preorder form
class PreorderTree(APIView):
    name = 'preorder-tree'

    def post(self, request):
        try:
            data = request.data
            tree_name = data['tree']
            try:
                tree = Tree.objects.get(name=tree_name)
                if tree:
                    t = BinarySearchTree()
                    for n in tree.data:
                        t.insert(n)
                    print(t.__str__())
                    list_tree = t.traversalTree(InPreOrder, t.root)
                    return Response({'tree': tree.name, 'preorder': list_tree}, status=200)
            except Exception as e:
                return Response({'Tree matching query does not exist'}, status=404)
        except Exception as e:
            return Response({'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)


# This class is a view show the max value in Tree
class MaxTree(APIView):
    name = 'max-value-tree'

    def post(self, request):
        try:
            data = request.data
            tree_name = data['tree']
            try:
                tree = Tree.objects.get(name=tree_name)
                if tree:
                    t = BinarySearchTree()
                    for n in tree.data:
                        t.insert(n)
                    val_max = t.getMax().getLabel()
                    return Response({'tree': tree.name, 'max_value': val_max}, status=200)
            except Exception as e:
                return Response({'Tree matching query does not exist'}, status=404)
        except Exception as e:
            return Response({'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)


# This class is a view show the min value in Tree
class MinTree(APIView):
    name = 'min-value-tree'

    def post(self, request):
        try:
            data = request.data
            tree_name = data['tree']
            try:
                tree = Tree.objects.get(name=tree_name)
                if tree:
                    t = BinarySearchTree()
                    for n in tree.data:
                        t.insert(n)
                    val_min = t.getMin().getLabel()
                    return Response({'tree': tree.name, 'min_value': val_min}, status=200)
            except Exception as e:
                return Response({'Tree matching query does not exist'}, status=404)
        except Exception as e:
            return Response({'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)


# This class is a view show the Lowest Common Ancestor in two nodes of Tree
class LowestCommonAncestor(APIView):
    name = 'lowest-common-ancestor'

    def post(self, request):
        """
            This End Point Return the Lowest Common Ancestor evaluated two nodes of tree.

            ---
            parameters:
            - name: body
              description: JSON object containing two strings: password and username.
              required: true
              paramType: body
              pytype: RequestSerializer
        """
        try:
            data = request.data
            tree_name = data['tree']
            node_one = data['node_one']
            node_two = data['node_two']
            try:
                tree = Tree.objects.get(name=tree_name)
                t = BinarySearchTree()
                for n in tree.data:
                    t.insert(n)
                if t.getNode(node_one) is not None and t.getNode(node_two) is not None:
                    LCA = t.findLCA(t.getRoot(), node_one, node_two)
                    return Response({'tree': tree.name, 'lowest-common-ancestor': LCA.getLabel()}, status=200)
                else:
                    return Response({'Node(s) does not exist'}, status=404)
            except Exception as e:
                print(e)
                return Response({'Tree matching query does not exist'}, status=404)
        except Exception as e:
            return Response({'BAD_REQUEST'}, status=status.HTTP_400_BAD_REQUEST)
