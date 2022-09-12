from django.db import models


# Create your models here.
# 创建文章表

class InteractionInfo(models.Model):
    Interaction_text = models.TextField(verbose_name="文章文字", )
    Interaction_img = models.URLField(verbose_name="图片路径")
    Interaction_time = models.TimeField(verbose_name="发表时间")
    Interaction_good = models.IntegerField(verbose_name="认同点赞")
    Interaction_bad = models.IntegerField(verbose_name="不认同点踩")

    # 无约束关联
    # xxx_name = models.BigIntegerField(verbose_name="id")

    # 有约束，删除操作时级联删除
    #   users = models.ForeignKey(to="users", to_field="id",on_delete=models.CASCADE())
    # 有约束关联，to=""关联哪张表 ，to_field=""关联表中的什么，如果用户注销了，文章不删除，只置空
    user = models.ForeignKey(to="users.UsersInfo", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
