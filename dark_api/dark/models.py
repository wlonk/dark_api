from django.conf import settings
from django.db import models, transaction
from django.utils.functional import cached_property


class SheetQuerySet(models.QuerySet):
    def create_sheet_for_user(self, user):
        with transaction.atomic():
            sheet = self.create(user=user, name='Thief', look='')
            for suit_name in ['spades', 'hearts', 'clubs', 'diamonds']:
                suit = Suit.objects.create(sheet=sheet, name=suit_name)
                AceCard.objects.create(suit=suit)
                for face_name in ['jack', 'queen', 'king']:
                    FaceCard.objects.create(suit=suit, name=face_name)
                BaseCard.objects.create(suit=suit)

            knowledges = SkillGroup.objects.create(name='Knowledges', sheet=sheet)
            Skill.objects.create(name="Arcana", skill_group=knowledges)
            Skill.objects.create(name="Art", skill_group=knowledges)
            Skill.objects.create(name="Craft", skill_group=knowledges)
            Skill.objects.create(name="Culture", skill_group=knowledges)
            Skill.objects.create(name="Enginery", skill_group=knowledges)
            Skill.objects.create(name="Finance", skill_group=knowledges)
            Skill.objects.create(name="History", skill_group=knowledges)
            Skill.objects.create(name="Medicine", skill_group=knowledges)
            Skill.objects.create(name="Politics", skill_group=knowledges)
            Skill.objects.create(name="Ranger", skill_group=knowledges)
            Skill.objects.create(name="Religion", skill_group=knowledges)
            Skill.objects.create(name="Sciences", skill_group=knowledges)

            social = SkillGroup.objects.create(name='Social', sheet=sheet)
            Skill.objects.create(name="Charm", skill_group=social)
            Skill.objects.create(name="Fellowship", skill_group=social)
            Skill.objects.create(name="Intimidate", skill_group=social)
            Skill.objects.create(name="Plead", skill_group=social)
            Skill.objects.create(name="Reassure", skill_group=social)
            Skill.objects.create(name="Respect", skill_group=social)

            physical = SkillGroup.objects.create(name='Physical', sheet=sheet)
            Skill.objects.create(name="Combat", skill_group=physical)
            Skill.objects.create(name="Traverse", skill_group=physical)
            return sheet


class Sheet(models.Model):
    objects = SheetQuerySet.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=128)
    look = models.TextField()

    @cached_property
    def suits(self):
        return self.suit_set.all()

    @cached_property
    def spades(self):
        return self.suit_set.filter(name='spades').first()

    @cached_property
    def hearts(self):
        return self.suit_set.filter(name='hearts').first()

    @cached_property
    def clubs(self):
        return self.suit_set.filter(name='clubs').first()

    @cached_property
    def diamonds(self):
        return self.suit_set.filter(name='diamonds').first()

    @cached_property
    def skill_groups(self):
        return self.skillgroup_set.all()


class Suit(models.Model):
    name = models.CharField(max_length=128)
    sheet = models.ForeignKey(Sheet)

    @cached_property
    def jack(self):
        return self.facecard_set.filter(name='jack').first()

    @cached_property
    def queen(self):
        return self.facecard_set.filter(name='queen').first()

    @cached_property
    def king(self):
        return self.facecard_set.filter(name='king').first()

    @cached_property
    def face_cards(self):
        return self.facecard_set.all()


class AceCard(models.Model):
    suit = models.OneToOneField(Suit, related_name='ace')
    value = models.IntegerField(default=0)


class FaceCard(models.Model):
    suit = models.ForeignKey(Suit)
    name = models.CharField(max_length=128)
    value = models.IntegerField(default=4)
    ability = models.CharField(max_length=128)
    advantage_1 = models.CharField(max_length=128)
    advantage_2 = models.CharField(max_length=128)
    advantage_3 = models.CharField(max_length=128)


class BaseCard(models.Model):
    suit = models.OneToOneField(Suit, related_name='base_card')
    value = models.IntegerField(default=4)


class SkillGroup(models.Model):
    sheet = models.ForeignKey(Sheet)
    name = models.CharField(max_length=128)

    @cached_property
    def skills(self):
        return self.skill_set.all()


class Skill(models.Model):
    skill_group = models.ForeignKey(SkillGroup)
    name = models.CharField(max_length=128)
    apt = models.BooleanField(default=False)
    edu = models.BooleanField(default=False)
    exp = models.BooleanField(default=False)
    acc = models.BooleanField(default=False)
