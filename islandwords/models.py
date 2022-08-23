from django.db import models


# Create your models here.

class IslandWords(models.Model):

    islandwordsTitle = models.CharField(verbose_name="岛话标题", max_length=100)
    islandwordsText = models.CharField(verbose_name="岛语文字", max_length=10000)

# 无约束关联
# xxx_name = models.BigIntegerField(verbose_name="id")

# 有约束，删除操作时级联删除
#   user = models.ForeignKey(to="users", to_field="id",on_delete=models.CASCADE())
# 有约束关联，to=""关联哪张表 ，to_field=""关联表中的什么，如果用户注销了，文章不删除，只置空
    user = models.ForeignKey(to="users.UserInfo", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)