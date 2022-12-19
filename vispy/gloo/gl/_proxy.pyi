class BaseGLProxy(object):
    def __call__(self, funcname, returns, *args): ...
    def glActiveTexture(self, texture): ...
    def glAttachShader(self, program, shader): ...
    def glBindAttribLocation(self, program, index, name): ...
    def glBindBuffer(self, target, buffer): ...
    def glBindFramebuffer(self, target, framebuffer): ...
    def glBindRenderbuffer(self, target, renderbuffer): ...
    def glBindTexture(self, target, texture): ...
    def glBlendColor(self, red, green, blue, alpha): ...
    def glBlendEquation(self, mode): ...
    def glBlendEquationSeparate(self, modeRGB, modeAlpha): ...
    def glBlendFunc(self, sfactor, dfactor): ...
    def glBlendFuncSeparate(self, srcRGB, dstRGB, srcAlpha, dstAlpha): ...
    def glBufferData(self, target, data, usage): ...
    def glBufferSubData(self, target, offset, data): ...
    def glCheckFramebufferStatus(self, target): ...
    def glClear(self, mask): ...
    def glClearColor(self, red, green, blue, alpha): ...
    def glClearDepth(self, depth): ...
    def glClearStencil(self, s): ...
    def glColorMask(self, red, green, blue, alpha): ...
    def glCompileShader(self, shader): ...
    def glCompressedTexImage2D(
        self, target, level, internalformat, width, height, border, data
    ): ...
    def glCompressedTexSubImage2D(
        self, target, level, xoffset, yoffset, width, height, format, data
    ): ...
    def glCopyTexImage2D(
        self, target, level, internalformat, x, y, width, height, border
    ): ...
    def glCopyTexSubImage2D(
        self, target, level, xoffset, yoffset, x, y, width, height
    ): ...
    def glCreateProgram(
        self,
    ): ...
    def glCreateShader(self, type): ...
    def glCullFace(self, mode): ...
    def glDeleteBuffer(self, buffer): ...
    def glDeleteFramebuffer(self, framebuffer): ...
    def glDeleteProgram(self, program): ...
    def glDeleteRenderbuffer(self, renderbuffer): ...
    def glDeleteShader(self, shader): ...
    def glDeleteTexture(self, texture): ...
    def glDepthFunc(self, func): ...
    def glDepthMask(self, flag): ...
    def glDepthRange(self, zNear, zFar): ...
    def glDetachShader(self, program, shader): ...
    def glDisable(self, cap): ...
    def glDisableVertexAttribArray(self, index): ...
    def glDrawArrays(self, mode, first, count): ...
    def glDrawElements(self, mode, count, type, offset): ...
    def glEnable(self, cap): ...
    def glEnableVertexAttribArray(self, index): ...
    def glFinish(
        self,
    ): ...
    def glFlush(
        self,
    ): ...
    def glFramebufferRenderbuffer(
        self, target, attachment, renderbuffertarget, renderbuffer
    ): ...
    def glFramebufferTexture2D(self, target, attachment, textarget, texture, level): ...
    def glFrontFace(self, mode): ...
    def glCreateBuffer(
        self,
    ): ...
    def glCreateFramebuffer(
        self,
    ): ...
    def glCreateRenderbuffer(
        self,
    ): ...
    def glCreateTexture(
        self,
    ): ...
    def glGenerateMipmap(self, target): ...
    def glGetActiveAttrib(self, program, index): ...
    def glGetActiveUniform(self, program, index): ...
    def glGetAttachedShaders(self, program): ...
    def glGetAttribLocation(self, program, name): ...
    def _glGetBooleanv(self, pname): ...
    def glGetBufferParameter(self, target, pname): ...
    def glGetError(
        self,
    ): ...
    def _glGetFloatv(self, pname): ...
    def glGetFramebufferAttachmentParameter(self, target, attachment, pname): ...
    def _glGetIntegerv(self, pname): ...
    def glGetProgramInfoLog(self, program): ...
    def glGetProgramParameter(self, program, pname): ...
    def glGetRenderbufferParameter(self, target, pname): ...
    def glGetShaderInfoLog(self, shader): ...
    def glGetShaderPrecisionFormat(self, shadertype, precisiontype): ...
    def glGetShaderSource(self, shader): ...
    def glGetShaderParameter(self, shader, pname): ...
    def glGetParameter(self, pname): ...
    def glGetTexParameter(self, target, pname): ...
    def glGetUniform(self, program, location): ...
    def glGetUniformLocation(self, program, name): ...
    def glGetVertexAttrib(self, index, pname): ...
    def glGetVertexAttribOffset(self, index, pname): ...
    def glHint(self, target, mode): ...
    def glIsBuffer(self, buffer): ...
    def glIsEnabled(self, cap): ...
    def glIsFramebuffer(self, framebuffer): ...
    def glIsProgram(self, program): ...
    def glIsRenderbuffer(self, renderbuffer): ...
    def glIsShader(self, shader): ...
    def glIsTexture(self, texture): ...
    def glLineWidth(self, width): ...
    def glLinkProgram(self, program): ...
    def glPixelStorei(self, pname, param): ...
    def glPolygonOffset(self, factor, units): ...
    def glReadPixels(self, x, y, width, height, format, type): ...
    def glRenderbufferStorage(self, target, internalformat, width, height): ...
    def glSampleCoverage(self, value, invert): ...
    def glScissor(self, x, y, width, height): ...
    def glShaderSource(self, shader, source): ...
    def glStencilFunc(self, func, ref, mask): ...
    def glStencilFuncSeparate(self, face, func, ref, mask): ...
    def glStencilMask(self, mask): ...
    def glStencilMaskSeparate(self, face, mask): ...
    def glStencilOp(self, fail, zfail, zpass): ...
    def glStencilOpSeparate(self, face, fail, zfail, zpass): ...
    def glTexImage2D(self, target, level, internalformat, format, type, pixels): ...
    def glTexParameterf(self, target, pname, param): ...
    def glTexParameteri(self, target, pname, param): ...
    def glTexSubImage2D(
        self, target, level, xoffset, yoffset, format, type, pixels
    ): ...
    def glUniform1f(self, location, v1): ...
    def glUniform2f(self, location, v1, v2): ...
    def glUniform3f(self, location, v1, v2, v3): ...
    def glUniform4f(self, location, v1, v2, v3, v4): ...
    def glUniform1i(self, location, v1): ...
    def glUniform2i(self, location, v1, v2): ...
    def glUniform3i(self, location, v1, v2, v3): ...
    def glUniform4i(self, location, v1, v2, v3, v4): ...
    def glUniform1fv(self, location, count, values): ...
    def glUniform2fv(self, location, count, values): ...
    def glUniform3fv(self, location, count, values): ...
    def glUniform4fv(self, location, count, values): ...
    def glUniform1iv(self, location, count, values): ...
    def glUniform2iv(self, location, count, values): ...
    def glUniform3iv(self, location, count, values): ...
    def glUniform4iv(self, location, count, values): ...
    def glUniformMatrix2fv(self, location, count, transpose, values): ...
    def glUniformMatrix3fv(self, location, count, transpose, values): ...
    def glUniformMatrix4fv(self, location, count, transpose, values): ...
    def glUseProgram(self, program): ...
    def glValidateProgram(self, program): ...
    def glVertexAttrib1f(self, index, v1): ...
    def glVertexAttrib2f(self, index, v1, v2): ...
    def glVertexAttrib3f(self, index, v1, v2, v3): ...
    def glVertexAttrib4f(self, index, v1, v2, v3, v4): ...
    def glVertexAttribPointer(self, indx, size, type, normalized, stride, offset): ...
    def glViewport(self, x, y, width, height): ...
