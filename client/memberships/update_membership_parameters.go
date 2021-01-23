// Code generated by go-swagger; DO NOT EDIT.

package memberships

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"context"
	"net/http"
	"time"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/runtime"
	cr "github.com/go-openapi/runtime/client"
	"github.com/go-openapi/strfmt"

	"github.com/t0mk/gometal/types"
)

// NewUpdateMembershipParams creates a new UpdateMembershipParams object
// with the default values initialized.
func NewUpdateMembershipParams() *UpdateMembershipParams {
	var ()
	return &UpdateMembershipParams{

		timeout: cr.DefaultTimeout,
	}
}

// NewUpdateMembershipParamsWithTimeout creates a new UpdateMembershipParams object
// with the default values initialized, and the ability to set a timeout on a request
func NewUpdateMembershipParamsWithTimeout(timeout time.Duration) *UpdateMembershipParams {
	var ()
	return &UpdateMembershipParams{

		timeout: timeout,
	}
}

// NewUpdateMembershipParamsWithContext creates a new UpdateMembershipParams object
// with the default values initialized, and the ability to set a context for a request
func NewUpdateMembershipParamsWithContext(ctx context.Context) *UpdateMembershipParams {
	var ()
	return &UpdateMembershipParams{

		Context: ctx,
	}
}

// NewUpdateMembershipParamsWithHTTPClient creates a new UpdateMembershipParams object
// with the default values initialized, and the ability to set a custom HTTPClient for a request
func NewUpdateMembershipParamsWithHTTPClient(client *http.Client) *UpdateMembershipParams {
	var ()
	return &UpdateMembershipParams{
		HTTPClient: client,
	}
}

/*UpdateMembershipParams contains all the parameters to send to the API endpoint
for the update membership operation typically these are written to a http.Request
*/
type UpdateMembershipParams struct {

	/*ID
	  Membership UUID

	*/
	ID strfmt.UUID
	/*Membership
	  Membership to update

	*/
	Membership *types.MembershipInput

	timeout    time.Duration
	Context    context.Context
	HTTPClient *http.Client
}

// WithTimeout adds the timeout to the update membership params
func (o *UpdateMembershipParams) WithTimeout(timeout time.Duration) *UpdateMembershipParams {
	o.SetTimeout(timeout)
	return o
}

// SetTimeout adds the timeout to the update membership params
func (o *UpdateMembershipParams) SetTimeout(timeout time.Duration) {
	o.timeout = timeout
}

// WithContext adds the context to the update membership params
func (o *UpdateMembershipParams) WithContext(ctx context.Context) *UpdateMembershipParams {
	o.SetContext(ctx)
	return o
}

// SetContext adds the context to the update membership params
func (o *UpdateMembershipParams) SetContext(ctx context.Context) {
	o.Context = ctx
}

// WithHTTPClient adds the HTTPClient to the update membership params
func (o *UpdateMembershipParams) WithHTTPClient(client *http.Client) *UpdateMembershipParams {
	o.SetHTTPClient(client)
	return o
}

// SetHTTPClient adds the HTTPClient to the update membership params
func (o *UpdateMembershipParams) SetHTTPClient(client *http.Client) {
	o.HTTPClient = client
}

// WithID adds the id to the update membership params
func (o *UpdateMembershipParams) WithID(id strfmt.UUID) *UpdateMembershipParams {
	o.SetID(id)
	return o
}

// SetID adds the id to the update membership params
func (o *UpdateMembershipParams) SetID(id strfmt.UUID) {
	o.ID = id
}

// WithMembership adds the membership to the update membership params
func (o *UpdateMembershipParams) WithMembership(membership *types.MembershipInput) *UpdateMembershipParams {
	o.SetMembership(membership)
	return o
}

// SetMembership adds the membership to the update membership params
func (o *UpdateMembershipParams) SetMembership(membership *types.MembershipInput) {
	o.Membership = membership
}

// WriteToRequest writes these params to a swagger request
func (o *UpdateMembershipParams) WriteToRequest(r runtime.ClientRequest, reg strfmt.Registry) error {

	if err := r.SetTimeout(o.timeout); err != nil {
		return err
	}
	var res []error

	// path param id
	if err := r.SetPathParam("id", o.ID.String()); err != nil {
		return err
	}

	if o.Membership != nil {
		if err := r.SetBodyParam(o.Membership); err != nil {
			return err
		}
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}
