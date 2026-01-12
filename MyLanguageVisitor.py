# Generated from MyLanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLanguageParser import MyLanguageParser
else:
    from MyLanguageParser import MyLanguageParser

# This class defines a complete generic visitor for a parse tree produced by MyLanguageParser.

class MyLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLanguageParser#program.
    def visitProgram(self, ctx:MyLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#block.
    def visitBlock(self, ctx:MyLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#descriptionList.
    def visitDescriptionList(self, ctx:MyLanguageParser.DescriptionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#nonEmptyTail.
    def visitNonEmptyTail(self, ctx:MyLanguageParser.NonEmptyTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#emptyTail.
    def visitEmptyTail(self, ctx:MyLanguageParser.EmptyTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#simpleDesc.
    def visitSimpleDesc(self, ctx:MyLanguageParser.SimpleDescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#arrayDesc.
    def visitArrayDesc(self, ctx:MyLanguageParser.ArrayDescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#simpleVarDescription.
    def visitSimpleVarDescription(self, ctx:MyLanguageParser.SimpleVarDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#typedArray.
    def visitTypedArray(self, ctx:MyLanguageParser.TypedArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#logicArray.
    def visitLogicArray(self, ctx:MyLanguageParser.LogicArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#type.
    def visitType(self, ctx:MyLanguageParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#identifierList.
    def visitIdentifierList(self, ctx:MyLanguageParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#nonEmptyTailId.
    def visitNonEmptyTailId(self, ctx:MyLanguageParser.NonEmptyTailIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#emptyTailId.
    def visitEmptyTailId(self, ctx:MyLanguageParser.EmptyTailIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#bounds.
    def visitBounds(self, ctx:MyLanguageParser.BoundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#statementList.
    def visitStatementList(self, ctx:MyLanguageParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#nonEmptyTailStmt.
    def visitNonEmptyTailStmt(self, ctx:MyLanguageParser.NonEmptyTailStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#emptyTailStmt.
    def visitEmptyTailStmt(self, ctx:MyLanguageParser.EmptyTailStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#assignStmt.
    def visitAssignStmt(self, ctx:MyLanguageParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#blockStmt.
    def visitBlockStmt(self, ctx:MyLanguageParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:MyLanguageParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#outputStmt.
    def visitOutputStmt(self, ctx:MyLanguageParser.OutputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#forStmt.
    def visitForStmt(self, ctx:MyLanguageParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#labelStmt.
    def visitLabelStmt(self, ctx:MyLanguageParser.LabelStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#conditionStmt.
    def visitConditionStmt(self, ctx:MyLanguageParser.ConditionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#ifStatement.
    def visitIfStatement(self, ctx:MyLanguageParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#outputStatement.
    def visitOutputStatement(self, ctx:MyLanguageParser.OutputStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#outputList.
    def visitOutputList(self, ctx:MyLanguageParser.OutputListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#nonEmptyTailOut.
    def visitNonEmptyTailOut(self, ctx:MyLanguageParser.NonEmptyTailOutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#emptyTailOut.
    def visitEmptyTailOut(self, ctx:MyLanguageParser.EmptyTailOutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#forStatement.
    def visitForStatement(self, ctx:MyLanguageParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#step.
    def visitStep(self, ctx:MyLanguageParser.StepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#loopBodyStmt.
    def visitLoopBodyStmt(self, ctx:MyLanguageParser.LoopBodyStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#loopBodyGoto.
    def visitLoopBodyGoto(self, ctx:MyLanguageParser.LoopBodyGotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#labelStatement.
    def visitLabelStatement(self, ctx:MyLanguageParser.LabelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#varId.
    def visitVarId(self, ctx:MyLanguageParser.VarIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#varConst.
    def visitVarConst(self, ctx:MyLanguageParser.VarConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#varArray.
    def visitVarArray(self, ctx:MyLanguageParser.VarArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#arrayVariable.
    def visitArrayVariable(self, ctx:MyLanguageParser.ArrayVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#indexWithVar.
    def visitIndexWithVar(self, ctx:MyLanguageParser.IndexWithVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#indexEmpty.
    def visitIndexEmpty(self, ctx:MyLanguageParser.IndexEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#constInt.
    def visitConstInt(self, ctx:MyLanguageParser.ConstIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#constReal.
    def visitConstReal(self, ctx:MyLanguageParser.ConstRealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#constString.
    def visitConstString(self, ctx:MyLanguageParser.ConstStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#expression.
    def visitExpression(self, ctx:MyLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#binaryOp.
    def visitBinaryOp(self, ctx:MyLanguageParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#emptyExprTail.
    def visitEmptyExprTail(self, ctx:MyLanguageParser.EmptyExprTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#fTailExpr.
    def visitFTailExpr(self, ctx:MyLanguageParser.FTailExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#fTailEmpty.
    def visitFTailEmpty(self, ctx:MyLanguageParser.FTailEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#condition.
    def visitCondition(self, ctx:MyLanguageParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#comparisonOp.
    def visitComparisonOp(self, ctx:MyLanguageParser.ComparisonOpContext):
        return self.visitChildren(ctx)



del MyLanguageParser