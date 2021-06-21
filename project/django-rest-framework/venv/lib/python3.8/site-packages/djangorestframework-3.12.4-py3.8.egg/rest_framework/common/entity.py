from dataclasses import dataclass


@dataclass
class FileDTO(object):

    context: str
    fname: str
    dframe: object

    @property # getter임
    def context(self) -> str: return self._context

    @context.setter # setter이며 따로 설정 이런 형식으로 함
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def dframe(self) -> str: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe