from django.conf import settings
from django.db import models, transaction
from django.utils.functional import cached_property


class SheetQuerySet(models.QuerySet):
    def create_sheet_for_user(self, user):
        with transaction.atomic():
            sheet = self.create(user=user, name='', look='')
            for suit_name in ['Spades', 'Hearts', 'Clubs', 'Diamonds']:
                suit = Suit.objects.create(sheet=sheet, name=suit_name)
                AceCard.objects.create(suit=suit)
                for face_name in ['Jack', 'Queen', 'King']:
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

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sheets')
    name = models.CharField(max_length=128, blank=True)
    look = models.TextField(blank=True)
    available_xp = models.IntegerField(default=0)

    @cached_property
    def total_xp(self):
        return sum(
            s.total_xp for s in self.suits.all()
        ) + sum(
            sg.total_xp for sg in self.skill_groups.all()
        )

    @cached_property
    def suits(self):
        return self.suit_set.all()

    @cached_property
    def spades(self):
        return self.suit_set.filter(name__iexact='spades').first()

    @cached_property
    def hearts(self):
        return self.suit_set.filter(name__iexact='hearts').first()

    @cached_property
    def clubs(self):
        return self.suit_set.filter(name__iexact='clubs').first()

    @cached_property
    def diamonds(self):
        return self.suit_set.filter(name__iexact='diamonds').first()

    @cached_property
    def skill_groups(self):
        return self.skillgroup_set.all()

    @cached_property
    def parent(self):
        return self.user


class Suit(models.Model):
    name = models.CharField(max_length=128)
    sheet = models.ForeignKey(Sheet)

    @cached_property
    def total_xp(self):
        return sum(
            fc.total_xp for fc in self.face_cards.all()
        ) + self.base_card.total_xp + self.ace.total_xp

    @cached_property
    def jack(self):
        return self.facecard_set.filter(name__iexact='jack').first()

    @cached_property
    def queen(self):
        return self.facecard_set.filter(name__iexact='queen').first()

    @cached_property
    def king(self):
        return self.facecard_set.filter(name__iexact='king').first()

    @cached_property
    def face_cards(self):
        return self.facecard_set.all()

    @cached_property
    def parent(self):
        return self.sheet


class AceCard(models.Model):
    suit = models.OneToOneField(Suit, related_name='ace')
    value = models.IntegerField(default=0)

    @cached_property
    def total_xp(self):
        return self.value

    @cached_property
    def parent(self):
        return self.suit


class FaceCard(models.Model):
    suit = models.ForeignKey(Suit)
    name = models.CharField(max_length=128)
    value = models.IntegerField(default=4)
    ability = models.CharField(max_length=128, blank=True)
    advantage_1 = models.CharField(max_length=128, blank=True)
    advantage_2 = models.CharField(max_length=128, blank=True)
    advantage_3 = models.CharField(max_length=128, blank=True)

    @cached_property
    def total_xp(self):
        advantage_sum = sum([
            bool(self.advantage_1),
            bool(self.advantage_2),
            bool(self.advantage_3),
        ])
        return self.value + advantage_sum - 4

    @cached_property
    def parent(self):
        return self.suit


class BaseCard(models.Model):
    suit = models.OneToOneField(Suit, related_name='base_card')
    value = models.IntegerField(default=4)

    @cached_property
    def total_xp(self):
        return self.value - 4

    @cached_property
    def parent(self):
        return self.suit


class SkillGroup(models.Model):
    sheet = models.ForeignKey(Sheet)
    name = models.CharField(max_length=128)

    @cached_property
    def total_xp(self):
        return sum(s.total_xp for s in self.skills.all())

    @cached_property
    def skills(self):
        return self.skill_set.all()

    @cached_property
    def parent(self):
        return self.sheet


class Skill(models.Model):
    skill_group = models.ForeignKey(SkillGroup)
    name = models.CharField(max_length=128)
    apt = models.BooleanField(default=False)
    edu = models.BooleanField(default=False)
    exp = models.BooleanField(default=False)
    acc = models.BooleanField(default=False)

    @cached_property
    def total_xp(self):
        return sum([
            self.apt,
            self.edu,
            self.exp,
            self.acc,
        ])

    @cached_property
    def parent(self):
        return self.skill_group
